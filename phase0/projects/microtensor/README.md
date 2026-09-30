# microtensor

Scalar autograd engine. A `Value` records the operation and inputs that
produced it; `backward()` topologically sorts that graph and applies the
chain rule to every node, accumulating gradients with `+=`. `Neuron`,
`Layer`, and `MLP` are built from `Value` operations alone. Phase 0 stretch
project, in the style of Karpathy's micrograd. Full spec:
`docs/phase0/projects.md`.

## Usage

```
cd phase0/projects
python -m microtensor.run_experiments
```

```python
from microtensor.engine import Value
from microtensor.nn import MLP

a = Value(2.0)
b = a * a + a.exp()
b.backward()
a.grad                      # 2*a + e**a

model = MLP(2, [4, 4, 1])   # ReLU hidden layers, linear output
for p in model.parameters():
    p.grad = 0.0            # zero before every backward()
```

## Structure

- `engine.py` — `Value`: `+`, `*`, `**`, `relu`, `exp`, `log`, derived ops (`-`, `/`, reflected dunders), `backward()`
- `nn.py` — `Neuron` (weights `uniform(-1, 1)`), `Layer`, `MLP`, each with `parameters()`
- `run_experiments.py` — the three checks below

## Results

- Gradient accumulation: `a * a` at `a = 2` gives `a.grad == 4.0`.
- Project 4's hand-worked example (2→2→2, softmax, cross-entropy): all 12 gradients match `TwoLayerNet.backward()`. The script asserts two of them (`W1[0][0]`, `W2[1][1]`).
- XOR, `MLP(2, [4, 4, 1])`, 37 parameters, 300 steps of GD at `lr=0.05`: loss 4.13 → ~1e-9, all four signs correct.

---

*Status: done — see `phase0/README.md`.*
