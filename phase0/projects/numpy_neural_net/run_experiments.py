import numpy as np
from .model import TwoLayerNet
from .layers import cross_entropy
from .train import train
from .visualize import plot_training_curves


def generate_synthetic_data(
    n_classes: int = 10,
    n_features: int = 30,
    n_samples_per_class: int = 200,
    center_scale: float = 1.0,
    noise_scale: float = 2.0,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray]:
    np.random.seed(seed)

    X_list = []
    y_list = []
    for class_idx in range(n_classes):
        center = np.random.randn(n_features) * center_scale
        points = center + np.random.randn(n_samples_per_class, n_features) * noise_scale
        labels = np.full(n_samples_per_class, class_idx)

        X_list.append(points)
        y_list.append(labels)

    X = np.vstack(X_list)
    y = np.concatenate(y_list)

    perm = np.random.permutation(len(X))
    X = X[perm]
    y = y[perm]

    return X, y


def main() -> None:
    X, y = generate_synthetic_data()
    split = int(0.8 * len(X))
    X_train, X_val = X[:split], X[split:]
    y_train, y_val = y[:split], y[split:]

    y_train_onehot = np.zeros((len(y_train), 10))
    y_train_onehot[np.arange(len(y_train)), y_train] = 1

    model = TwoLayerNet(30, 64, 10)
    probs, cache = model.forward(X_train)
    loss = cross_entropy(y_train_onehot, probs)
    assert np.isclose(loss, np.log(10), atol=0.05)

    grad_errors = model.gradient_check(X_train[:16], y_train_onehot[:16])
    assert all(err < 1e-4 for err in grad_errors.values())

    history = train(model, X_train, y_train_onehot, X_val, y_val, lr=0.01, n_epochs=30)
    assert history["val_accuracy"][-1] > 0.6
    plot_training_curves(history["train_loss"], history["val_accuracy"])


if __name__ == "__main__":
    main()
