import numpy as np


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(x, 0)


def relu_backward(dout: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, dout, 0)


def softmax(logits: np.ndarray) -> np.ndarray:
    logits_shifted = logits - logits.max(axis=-1, keepdims=True)
    exp_z = np.exp(logits_shifted)
    return exp_z / exp_z.sum(axis=-1, keepdims=True)


def cross_entropy(y_true_onehot: np.ndarray, probs: np.ndarray) -> np.ndarray:
    eps = 1e-9
    per_sample = -np.sum(y_true_onehot * np.log(probs + eps), axis=1)
    return np.mean(per_sample)
