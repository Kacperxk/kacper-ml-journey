import numpy as np
from .layers import relu, relu_backward, softmax, cross_entropy


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
        dW1 = cache["X"].T @ d_z1
        db1 = d_z1.sum(axis=0)
        return {"W1": dW1, "b1": db1, "W2": dW2, "b2": db2}

    def predict(self, X: np.ndarray) -> np.ndarray:
        probs = self.forward(X)[0]
        return probs.argmax(axis=1)

    def params(self) -> dict:
        return {"W1": self.W1, "b1": self.b1, "W2": self.W2, "b2": self.b2}

    def gradient_check(
        self, X: np.ndarray, y_true_onehot: np.ndarray, eps: float = 1e-5
    ) -> dict:
        cache = self.forward(X)[1]
        analytic_grads = self.backward(y_true_onehot, cache)

        relative_errors = {}

        for key in analytic_grads.keys():
            param = getattr(self, key)
            numeric = np.zeros_like(param)

            it = np.nditer(param, flags=["multi_index"])
            for _ in it:
                idx = it.multi_index
                original = param[idx]
                param[idx] = original + eps
                loss_plus = cross_entropy(y_true_onehot, self.forward(X)[0])
                param[idx] = original - eps
                loss_minus = cross_entropy(y_true_onehot, self.forward(X)[0])
                param[idx] = original
                numeric[idx] = (loss_plus - loss_minus) / (2 * eps)

            analytic = analytic_grads[key]
            relative_errors[key] = np.linalg.norm(numeric - analytic) / (
                np.linalg.norm(numeric) + np.linalg.norm(analytic)
            )

        return relative_errors
