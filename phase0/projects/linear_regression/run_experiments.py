import numpy as np
from .model import LinearRegression
from sklearn.datasets import fetch_california_housing
from .optimizers import vanilla_step, momentum_step, adam_step
from .visualize import (
    plot_loss_curves,
    plot_predictions_vs_truth,
    plot_weight_convergence,
    plot_optimizer_comparison,
)


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

    plot_weight_convergence(np.array(model_gd.weight_history))

    data = fetch_california_housing()
    X, y = data.data, data.target
    X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)
    model_housing = LinearRegression(method="gd", n_epochs=1000).fit(X_scaled, y)
    r2 = model_housing.score(X_scaled, y)
    y_pred = model_housing.predict(X_scaled)

    assert 0.5 < r2 < 0.7
    plot_predictions_vs_truth(y, y_pred)

    def toy_function(params: np.ndarray) -> float:
        x, y = params[0], params[1]
        return x**2 + 5 * y**2

    def toy_gradient(params: np.ndarray, noise_std: float = 2.0) -> np.ndarray:
        x, y = params[0], params[1]
        true_grad = np.array([2 * x, 10 * y])
        return true_grad + np.random.randn(2) * noise_std

    params = np.array([3.0, 3.0])
    vanilla_losses = []

    for _ in range(100):
        grad = toy_gradient(params)
        params = vanilla_step(params, grad, lr=0.02)
        vanilla_losses.append(toy_function(params))

    params = np.array([3.0, 3.0])
    velocity = np.zeros(2)
    momentum_losses = []

    for _ in range(100):
        grad = toy_gradient(params)
        params, velocity = momentum_step(params, grad, velocity, lr=0.02)
        momentum_losses.append(toy_function(params))

    params = np.array([3.0, 3.0])
    m = np.zeros(2)
    v = np.zeros(2)
    t = 0
    adam_losses = []

    for _ in range(100):
        grad = toy_gradient(params)
        t += 1
        params, m, v = adam_step(params, grad, m, v, t, lr=0.02)
        adam_losses.append(toy_function(params))

    optimizers = {
        "vanilla": vanilla_losses,
        "momentum": momentum_losses,
        "adam": adam_losses,
    }
    plot_optimizer_comparison(optimizers)

    # with a shared learning rate tuned for vanilla GD, Adam converges far slower on this simple,
    # low-noise-relative-to-signal toy problem, since it's normalized per-parameter step size
    # doesn't exploit the large early gradient magnitude the way vanilla/momentum do.
    # Adam's advantage shows up on noisier or messier loss surfaces, not here.


if __name__ == "__main__":
    main()
