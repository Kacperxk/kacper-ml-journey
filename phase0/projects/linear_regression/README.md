# Linear Regression from Scratch

`LinearRegression` in pure NumPy: closed-form least squares, batch and
mini-batch gradient descent, optional L2 (ridge) penalty, and three
optimizers (vanilla, momentum, Adam). Tested on synthetic data with known
weights and on California Housing. Full spec: `docs/phase0/projects.md`.
Write-up: `docs/phase0/linear_regression_project_explained.pdf`.

## Usage

```
cd phase0/projects
python -m linear_regression.run_experiments
```

```python
from linear_regression.model import LinearRegression

model = LinearRegression(method="gd", lr=0.01, n_epochs=1000, batch_size=32,
                         alpha=0.1, optimizer="adam").fit(X, y)
model.predict(X)
model.score(X, y)          # R²
model.loss_history         # mean MSE per epoch
```

`method="closed_form"` solves with `np.linalg.lstsq`; the GD options
(`lr`, `n_epochs`, `batch_size`, `alpha`, `optimizer`) apply only to
`method="gd"`. `batch_size=None` means full-batch GD.

## Structure

- `model.py` — `LinearRegression`: `fit`, `predict`, `score`
- `optimizers.py` — `vanilla_step`, `momentum_step`, `adam_step`, shared by the model and the toy-function comparison
- `metrics.py` — `r_squared`, `mse`
- `visualize.py` — the four plots, saved to `figures/` (gitignored)
- `run_experiments.py` — synthetic-data checks, ridge on collinear features, California Housing, optimizer comparison

## Results

- Synthetic data (`w = [2.5, -1.3, 0.7]`, `b = 4.0`): closed-form and GD both recover the weights within 0.1.
- Ridge (`alpha=0.1`) on a near-duplicate feature: total weight magnitude smaller than the unregularized fit.
- California Housing, standardized features, GD: R² ≈ 0.60 (closed-form: 0.61).
- Toy function `x² + 5y²` with noisy gradients, shared `lr=0.02`: Adam converges slowest. Its per-parameter normalized step doesn't use the large early gradients the way vanilla GD and momentum do.

California Housing is downloaded by scikit-learn on the first run and cached in `~/scikit_learn_data`.

## Known issue

Synthetic data isn't seeded, so about 1 run in 20 fails the closed-form
`atol=0.1` assert on sampling noise alone.

---

*Status: done — see `phase0/README.md`.*
