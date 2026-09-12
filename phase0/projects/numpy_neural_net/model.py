import numpy as np
from .layers import relu, relu_backward, softmax


class TwoLayerNet:
    def __init__(
        self, n_features: int, n_hidden: int, n_classes: int, seed: int = 42
    ) -> None:
        np.random.seed(seed)
        self.W1 = np.random.randn(n_features, n_hidden) * 0.01
        self.W2 = np.random.randn(n_hidden, n_classes) * 0.01
        self.b1 = np.zeros(shape=(n_hidden,))
        self.b2 = np.zeros(shape=(n_classes,))

    def forward(self, X: np.ndarray) -> tuple[np.ndarray, dict]:
        z1 = X @ self.W1 + self.b1
        a1 = relu(z1)
        z2 = a1 @ self.W2 + self.b2
        probs = softmax(z2)
        cache = {"X": X, "z1": z1, "a1": a1, "z2": z2, "probs": probs}

        return probs, cache

    def backward(self, y_true_onehot: np.ndarray, cache: dict) -> dict:
        n = y_true_onehot.shape[0]
        d_logits = (cache["probs"] - y_true_onehot) / n
        dW2 = cache["a1"].T @ d_logits
        db2 = d_logits.sum(axis=0)
        d_a1 = d_logits @ self.W2.T
        d_z1 = relu_backward(d_a1, cache["z1"])
