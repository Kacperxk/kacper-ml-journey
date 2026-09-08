import numpy as np
from .model import LinearRegression
from .visualize import plot_loss_curves


def main() -> None:
    X = np.random.randn(200, 3)
    true_w = np.array([2.5, -1.3, 0.7])
    true_b = 4.0
    noise = np.random.randn(200) * 0.5
    y = X @ true_w + true_b + noise

    model_cf = LinearRegression(method="closed_form").fit(X, y)
    assert np.allclose(true_w, model_cf.w, atol=0.1)
    assert np.isclose(true_b, model_cf.b, atol=0.1)

    model_gd = LinearRegression(method="gd", n_epochs=1000).fit(X, y)
    assert np.allclose(true_w, model_gd.w, atol=0.1)
    assert np.isclose(true_b, model_gd.b, atol=0.1)

    batch_gd = LinearRegression(method="gd").fit(X, y)
    mini_batch_gd = LinearRegression(method="gd", batch_size=32).fit(X, y)
    plot_loss_curves(batch_gd.loss_history, mini_batch_gd.loss_history)

    X_collinear = X.copy()
    X_collinear[:, 0] = X_collinear[:, 0] + np.random.randn(200) * 0.01
    X_extended = np.hstack([X, X_collinear[:, [0]]])
    model_ridge = LinearRegression(method="gd", alpha=0.1, n_epochs=1000).fit(
        X_extended, y
    )
    model_plain = LinearRegression(method="gd", alpha=0.0, n_epochs=1000).fit(
        X_extended, y
    )
    assert np.abs(model_ridge.w).sum() < np.abs(model_plain.w).sum()


if __name__ == "__main__":
    main()
