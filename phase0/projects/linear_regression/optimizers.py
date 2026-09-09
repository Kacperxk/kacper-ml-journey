import numpy as np


def vanilla_step(params: np.ndarray, grad: np.ndarray, lr: float) -> np.ndarray:
    return params - grad * lr


def momentum_step(
    params: np.ndarray,
    grad: np.ndarray,
    velocity: np.ndarray,
    lr: float,
    beta: float = 0.9,
) -> tuple[np.ndarray, np.ndarray]:
    velocity = beta * velocity + (1 - beta) * grad
    params = params - lr * velocity
    return params, velocity


def adam_step(
    params: np.ndarray,
    grad: np.ndarray,
    m: np.ndarray,
    v: np.ndarray,
    t: int,
    lr: float,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * grad**2
    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)
    params = params - lr * m_hat / (np.sqrt(v_hat) + eps)
    return params, m, v
