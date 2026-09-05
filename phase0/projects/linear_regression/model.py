import numpy as np
from .metrics import r_squared


class LinearRegression:
    def __init__(
        self,
        method: str = "gd",
        lr: float = 0.01,
        n_epochs: int = 100,
        batch_size: int | None = None,
        alpha: float = 0.0,
        optimizer: str = "vanilla",
        seed: int = 42,
    ) -> None:
        self.method = method
        self.lr = lr
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.alpha = alpha
        self.optimizer = optimizer
        self.seed = seed
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        self._fit_closed_form(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return X @ self.w + self.b

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        y_pred = self.predict(X)
        return r_squared(y, y_pred)

    def _fit_closed_form(self, X: np.ndarray, y: np.ndarray) -> None:
        ones = np.ones((X.shape[0], 1))
        X_aug = np.hstack([X, ones])
        coef, residuals, rank, s = np.linalg.lstsq(X_aug, y, rcond=None)
        self.w = coef[:-1]
        self.b = coef[-1]
