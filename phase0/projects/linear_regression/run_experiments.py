import numpy as np
from .model import LinearRegression


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


if __name__ == "__main__":
    main()
