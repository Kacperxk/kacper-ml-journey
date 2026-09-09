import numpy as np


def vanilla_step(params: np.ndarray, grad: np.ndarray, lr: float) -> np.ndarray:
    return params - grad * lr
