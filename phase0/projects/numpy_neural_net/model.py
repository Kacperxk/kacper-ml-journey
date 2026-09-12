import numpy as np
from .layers import relu, softmax


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
