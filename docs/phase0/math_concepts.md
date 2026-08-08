# Phase 0 — Math Concepts

Linear algebra, calculus, and probability, connected directly to ML code.
No separate drills file for math — the "formula → code" habit described here
is the practice.

---

## The Right Mindset

Your econometrics degree means you know most of this math already. The goal is not to learn new material — it is to connect what you know to how it appears in ML code. For every formula you review, implement it in NumPy. This habit of "formula → code" is the core skill of ML engineering.

---

## 1.1 — Linear Algebra: The ML Perspective

### Why every ML operation is linear algebra

A dataset of 1000 samples with 50 features is a matrix X of shape (1000, 50). A linear layer applies `output = X @ W + b`. Training is finding W and b that make this useful. Every layer in a neural network is one of these matrix operations chained together.

### Matrix multiplication — what it actually computes

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])    # shape (3, 2)

C = A @ B    # shape (2, 2)
# C[0,0] = 1*7 + 2*9 + 3*11 = 58
# C[0,1] = 1*8 + 2*10 + 3*12 = 64
# C[i,j] = dot product of row i of A with column j of B
```

### Eigenvalues and eigenvectors — geometric meaning

If `M @ v = λ * v`, then v is an eigenvector of M. Multiplying M by v only scales v (by λ) — it does not rotate it. Eigenvectors are the "special directions" that a matrix only stretches.

In ML: PCA finds the directions (eigenvectors of the covariance matrix) along which data varies most. The eigenvalue tells you how much variance is in each direction.

```python
X = np.random.randn(100, 3)    # 100 samples, 3 features
cov = np.cov(X.T)              # covariance matrix, shape (3, 3)

eigenvalues, eigenvectors = np.linalg.eig(cov)

# Sort by variance (largest eigenvalue first)
idx = np.argsort(eigenvalues)[::-1]
top_2 = eigenvectors[:, idx[:2]]   # top 2 directions

X_2d = X @ top_2   # shape (100, 2) — projected onto 2 most-important dimensions
```

### SVD — decompose any matrix

`M = U @ np.diag(S) @ Vt` where U and Vt have orthogonal columns, S contains singular values (non-negative, sorted descending).

In ML: SVD appears in LoRA (fine-tuning method that decomposes weight updates into low-rank matrices), in PCA (numerically better implementation), and in attention mechanisms.

```python
M = np.random.randn(5, 3)
U, S, Vt = np.linalg.svd(M, full_matrices=False)
# U: (5,3)  S: (3,)  Vt: (3,3)

M_reconstructed = U @ np.diag(S) @ Vt
print(np.allclose(M, M_reconstructed))   # True

# Low-rank approximation — keep only top k singular values
k = 2
M_approx = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
# Same shape (5, 3) but approximate
```

---

## 1.2 — Calculus: Backpropagation Intuition

### The gradient — direction of steepest increase

For f(x), the gradient ∇f(x) points where f increases fastest. To minimize f, move in the opposite direction. This is gradient descent.

```python
def f(params):
    x, y = params[0], params[1]
    return x**2 + y**2   # bowl shape, minimum at (0, 0)

def grad_f(params):
    x, y = params[0], params[1]
    return np.array([2*x, 2*y])   # df/dx=2x, df/dy=2y

params = np.array([3.0, -2.0])
lr = 0.1

for step in range(30):
    gradient = grad_f(params)
    params = params - lr * gradient   # move against the gradient
    if step % 10 == 0:
        print(f"Step {step}: loss={f(params):.4f}, params={params.round(3)}")
# Converges to [0, 0]
```

### The chain rule — this is backpropagation

If `y = f(g(x))`, then `dy/dx = f'(g(x)) * g'(x)`.

In a neural network: `loss = Loss(Activation(Linear(x)))`. The chain rule tells you how to propagate the error signal backward through each function. PyTorch's `.backward()` automates this. Understanding it manually makes you a much better debugger.

```python
# Manual backprop through: loss = (relu(w*x + b) - y_true)^2

x = 2.0;  w = 3.0;  b = 1.0;  y_true = 5.0

# FORWARD PASS
z = w * x + b            # z = 7.0
a = max(0.0, z)          # a = 7.0  (relu)
loss = (a - y_true)**2   # loss = 4.0

# BACKWARD PASS — chain rule
d_loss_d_a = 2 * (a - y_true)         # df/da = 2*(7-5) = 4.0
d_a_d_z   = 1.0 if z > 0 else 0.0    # drelu/dz = 1 (since z>0)
d_z_d_w   = x                          # dz/dw = x = 2.0

# Chain: d_loss/d_w = d_loss/d_a * d_a/d_z * d_z/d_w
d_loss_d_w = d_loss_d_a * d_a_d_z * d_z_d_w   # 4*1*2 = 8.0

# Update
w_new = w - 0.01 * d_loss_d_w   # 3.0 - 0.08 = 2.92
```

PyTorch's `.backward()` does exactly this for every parameter simultaneously.

### Gradient descent variants

- **Batch GD**: gradient over all n samples per update. Accurate but slow for large n.
- **SGD**: gradient over 1 sample per update. Fast but very noisy.
- **Mini-batch GD**: gradient over a small batch (32–512). The standard. Best balance.

---

## 1.3 — Probability: The Language of ML

### Softmax — turning numbers into probabilities

A model's final layer outputs raw scores (logits). Softmax converts them to probabilities: all positive, all sum to 1.

Formula: `softmax(z)_i = exp(z_i) / sum_j(exp(z_j))`

```python
def softmax(logits):
    # Numerically stable — subtract max first to avoid exp overflow
    # Mathematical result is identical
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exp_z = np.exp(shifted)
    return exp_z / exp_z.sum(axis=-1, keepdims=True)

logits = np.array([2.0, 1.0, 0.5])
probs = softmax(logits)
print(probs)           # [0.59, 0.24, 0.17]
print(probs.sum())     # 1.0
```

### Cross-entropy loss

Measures how well a predicted probability matches the true class.

For classification: `loss = -log(probability assigned to the correct class)`

Intuition:
- Model assigns 0.99 to correct class: `loss = -log(0.99) ≈ 0.01` — good
- Model assigns 0.01 to correct class: `loss = -log(0.01) ≈ 4.6` — bad

```python
def cross_entropy(y_true_onehot, y_pred_probs):
    """
    y_true_onehot: shape (n, classes) — one-hot encoded labels
    y_pred_probs:  shape (n, classes) — softmax probabilities
    """
    eps = 1e-9   # prevent log(0)
    per_sample = -np.sum(y_true_onehot * np.log(y_pred_probs + eps), axis=1)
    return np.mean(per_sample)

y_true = np.array([[1,0,0], [0,1,0], [0,0,1]])

y_good = np.array([[0.9, 0.05, 0.05],
                   [0.05, 0.9, 0.05],
                   [0.05, 0.05, 0.9]])

y_bad  = np.array([[0.33, 0.33, 0.34],
                   [0.33, 0.34, 0.33],
                   [0.34, 0.33, 0.33]])

print(cross_entropy(y_true, y_good))   # ~0.105 — low, good
print(cross_entropy(y_true, y_bad))    # ~1.099 — high, bad
```

### Why cross-entropy equals MLE

Maximum Likelihood Estimation: find parameters θ maximizing `P(data | θ)`.
Take log: `maximize sum_i log P(sample_i | θ)`.
Negate (optimizers minimize): `minimize -sum_i log P(sample_i | θ)`.
For classifiers, `P(sample_i | θ)` = predicted probability of the correct class.
Result: `minimize -sum_i log(predicted_correct_prob_i)` — this IS cross-entropy.

The loss function is not arbitrary. It is MLE written in code form.

### KL Divergence

Measures how different two distributions P and Q are:
`KL(P || Q) = sum_i P_i * log(P_i / Q_i)`

Always ≥ 0. Equals 0 only when P = Q. Not symmetric.

You will see KL divergence in: variational autoencoders, RLHF (keeping the new policy close to the reference model), knowledge distillation.

```python
def kl_divergence(P, Q):
    eps = 1e-9
    return np.sum(P * np.log((P + eps) / (Q + eps)))

P = np.array([0.4, 0.4, 0.2])
Q = np.array([0.35, 0.4, 0.25])   # close
R = np.array([0.1, 0.1, 0.8])     # far

print(kl_divergence(P, Q))   # small
print(kl_divergence(P, R))   # large
print(kl_divergence(P, P))   # 0.0
```

---

## 1.4 — Resources for Math

- *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — free PDF at mml-book.github.io. Directly connects math to ML. With your background you can move fast.
- 3Blue1Brown "Essence of Linear Algebra" on YouTube — visual intuition first.
- 3Blue1Brown "Neural Networks" series — builds intuition for calculus in backprop.
- StatQuest with Josh Starmer on YouTube — probability and statistics with extraordinary clarity.

---

*Last updated: 2026-08-08*
