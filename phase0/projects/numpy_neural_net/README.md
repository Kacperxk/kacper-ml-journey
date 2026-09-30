# NumPy Neural Network

`TwoLayerNet` — `Linear → ReLU → Linear → Softmax` with cross-entropy loss —
in pure NumPy, with a hand-derived backward pass, a finite-difference
gradient check, and mini-batch SGD. Phase 0 capstone. Full spec:
`docs/phase0/projects.md`. Write-up:
`docs/phase0/NumPy_Neural_Network_project_explained.pdf`.

## Usage

```
cd phase0/projects
python -m numpy_neural_net.run_experiments
```

```python
from numpy_neural_net.model import TwoLayerNet
from numpy_neural_net.train import train

model = TwoLayerNet(n_features=30, n_hidden=64, n_classes=10)
model.gradient_check(X[:16], y_onehot[:16])   # relative error per parameter
history = train(model, X_train, y_train_onehot, X_val, y_val, lr=0.01, n_epochs=30)
model.predict(X_val)
```

## Structure

- `layers.py` — `relu`, `relu_backward`, `softmax` (subtract-max), `cross_entropy`
- `model.py` — `TwoLayerNet`: `forward` (returns probs + cache), `backward`, `predict`, `params`, `gradient_check`
- `train.py` — mini-batch SGD loop, reshuffled every epoch
- `visualize.py` — train loss and val accuracy curves, saved to `figures/` (gitignored)
- `run_experiments.py` — synthetic 10-class data (30 features, 2000 points), 80/20 split, the checks below

## Results

- Loss at initialization: 2.3028, vs. log(10) ≈ 2.3026 for a uniform guess over 10 classes.
- Gradient check: relative error ~5e-9 on `W1`, `b1`, `W2`, `b2` (bar: 1e-4).
- After 30 epochs at `lr=0.01`: val accuracy ~0.83 (bar: 0.6); train loss 2.30 → 0.51.

---

*Status: done — see `phase0/README.md`.*
