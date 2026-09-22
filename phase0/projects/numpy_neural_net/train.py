import numpy as np
from .model import TwoLayerNet
from .layers import cross_entropy


def train(
    model: "TwoLayerNet",
    X_train: np.ndarray,
    y_train_onehot: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    lr: float = 0.5,
    batch_size: int = 32,
    n_epochs: int = 30,
) -> dict:
    train_loss = []
    val_accuracy = []

    for epoch in range(n_epochs):
        batch_loss = []
        indices = np.random.permutation(X_train.shape[0])
        X_shuffled = X_train[indices]
        y_shuffled = y_train_onehot[indices]
        for batch in range(0, X_train.shape[0], batch_size):
            X_batch = X_shuffled[batch : batch + batch_size]
            y_batch = y_shuffled[batch : batch + batch_size]
            probs, cache = model.forward(X_batch)
            grads = model.backward(y_batch, cache)
            params = model.params()
            for name in params:
                params[name] -= lr * grads[name]

            batch_loss.append(cross_entropy(y_batch, probs))
        train_loss.append(np.mean(batch_loss))

        preds = model.predict(X_val)
        val_accuracy.append((preds == y_val).mean())

    return {"train_loss": train_loss, "val_accuracy": val_accuracy}
