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
