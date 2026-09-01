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

For f(x), the gradient ∇f(x) points where f increases fastest. To minimize f, move in the opposite direction. This is gradient descent. `lr` (**learning rate**) scales how big each step is: too high and updates overshoot and can diverge or oscillate; too low and convergence is needlessly slow. It's the first hyperparameter — a value you choose before training, as opposed to a parameter the model learns — you'll tune by hand.

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

### Matrix calculus — gradients w.r.t. a matrix

The chain rule above was scalar. `W` in `y = x @ W + b` is a whole matrix —
`dL/dW` has the same shape as `W`. The practical shortcut: **shape-matching**.
Given the upstream gradient `d_out = dL/dy` (same shape as `y`), there's
usually only one way to multiply it against the other known arrays that
produces the right shape — that multiplication is the gradient.

```python
# y = x @ W + b
# x: (n, in)   W: (in, out)   b: (out,)   y, d_out: (n, out)
np.random.seed(0)
x = np.random.randn(4, 3)      # n=4, in=3
W = np.random.randn(3, 5)      # in=3, out=5
b = np.random.randn(5)
y_true = np.random.randn(4, 5)

y = x @ W + b
d_out = 2 / y.size * (y - y_true)   # dL/dy for MSE loss

d_x = d_out @ W.T          # (4,5) @ (5,3) -> (4,3)  — matches x's shape
d_W = x.T @ d_out          # (3,4) @ (4,5) -> (3,5)  — matches W's shape
d_b = d_out.sum(axis=0)    # (5,) — matches b's shape; sum over the batch
                             # axis because every sample's error contributed
                             # to the same shared bias

# Verify d_W against a finite-difference numerical gradient
eps = 1e-5
num_dW = np.zeros_like(W)
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        W[i, j] += eps
        loss_plus = np.mean((x @ W + b - y_true) ** 2)
        W[i, j] -= 2 * eps
        loss_minus = np.mean((x @ W + b - y_true) ** 2)
        W[i, j] += eps                       # restore
        num_dW[i, j] = (loss_plus - loss_minus) / (2 * eps)

print(np.allclose(num_dW, d_W, atol=1e-5))   # True
```

`allclose` is enough for a quick check, but gradient checks are more often reported as a single **relative error**, since it stays meaningful whether the gradient values are tiny or huge (a fixed absolute tolerance doesn't):

```
rel_error = norm(numeric_grad - analytic_grad) / (norm(numeric_grad) + norm(analytic_grad))
```

```python
rel_error = np.linalg.norm(num_dW - d_W) / (np.linalg.norm(num_dW) + np.linalg.norm(d_W))
print(rel_error)   # ~2e-11 — well under the usual 1e-4 pass/fail threshold
```

### Gradient descent variants

One **epoch** is one full pass through the entire training set. `n_epochs=30` means the training loop sees every training sample 30 times, split across however many batches it takes to cover them.

- **Batch GD**: gradient over all n samples per update. Accurate but slow for large n.
- **SGD**: gradient over 1 sample per update. Fast but very noisy.
- **Mini-batch GD**: gradient over a small batch (32–512). The standard. Best balance.

### Momentum and Adam — smoothing out noisy gradients

Mini-batch and SGD gradients are noisy estimates of the true gradient — each batch only sees a slice of the data. **Momentum** keeps a running average of past gradients (a "velocity") and steps with that instead of the raw noisy gradient:

```
v = β * v + (1 - β) * grad
params = params - lr * v
```

β (typically 0.9) controls how much history to keep. Averaging over recent gradients cancels out noise that points in random directions while reinforcing the direction the gradient consistently agrees on.

**Adam** tracks both a momentum-style average of the gradient (first moment `m`) and an average of the *squared* gradient (second moment `v`), then divides the step by the square root of the second moment — giving each parameter its own adaptive step size:

```
m = β1*m + (1-β1)*grad              # mean of gradients
v = β2*v + (1-β2)*grad**2           # mean of squared gradients
m_hat = m / (1 - β1**t)             # bias correction — m, v start at 0
v_hat = v / (1 - β2**t)
params = params - lr * m_hat / (sqrt(v_hat) + eps)
```

Common defaults: β1=0.9, β2=0.999, eps=1e-8.

In ML: Adam (or a close variant) is the default optimizer for most neural network training. But adaptive methods aren't automatically better — on a small, smooth, noise-free problem, a well-tuned plain gradient descent can match or beat them. Momentum and Adam earn their keep specifically when gradients are noisy (mini-batches) or the loss surface is large and messy (real neural networks). Verify this yourself rather than assuming it:

```python
def f(params):
    x, y = params
    return x**2 + 5*y**2

def noisy_grad(params, noise_std=1.0):
    x, y = params
    true_grad = np.array([2*x, 10*y])
    return true_grad + np.random.randn(2) * noise_std   # simulates a noisy mini-batch estimate

start = np.array([3.0, 3.0])
lr = 0.05

# Vanilla GD on noisy gradients
np.random.seed(0)
params = start.copy()
for _ in range(100):
    params = params - lr * noisy_grad(params)
print(f(params))   # ~0.034

# Momentum on the exact same noisy gradients
np.random.seed(0)
params = start.copy()
v = np.zeros(2)
beta = 0.9
for _ in range(100):
    grad = noisy_grad(params)
    v = beta * v + (1 - beta) * grad
    params = params - lr * v
print(f(params))   # ~0.020 — momentum's averaging cancels noise vanilla GD reacts to directly
```

---

## 1.3 — Probability: The Language of ML

### Expectation, variance, and covariance

Expectation `E[X]` is the probability-weighted average outcome of a random variable — for a sample of data, the empirical estimate is just the mean. Variance `Var(X) = E[(X - E[X])^2]` measures spread around that mean; standard deviation is its square root, in the same units as X. Covariance measures how two variables move together: `Cov(X,Y) = E[(X-E[X])(Y-E[Y])]` — positive means they rise and fall together, negative means one rises as the other falls, near-zero means no linear relationship.

In ML: a loss function averaged over a batch (`np.mean(losses)`) is an empirical estimate of an expectation over the data distribution — this is what "expected loss" / "risk" means. Variance shows up in weight initialization (Xavier/Kaiming scale weights by variance to keep activations stable across layers) and in batch norm. The covariance matrix is exactly what `np.cov` computed in the PCA example above — this is the formal definition behind that call.

```python
X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
mean = X.mean()          # 3.0 — E[X]
var = X.var()             # 2.0 — average squared distance from the mean
std = X.std()              # 1.414 — sqrt(var)

Y = 2 * X                                  # moves perfectly with X
Z = np.array([5.0, 1.0, 4.0, 2.0, 3.0])   # unrelated to X

print(np.cov(X, Y)[0, 1])   # 5.0  — strongly positive: X and Y move together
print(np.cov(X, Z)[0, 1])   # -0.75 — near zero: little linear relationship
```

### Bayes' theorem

Bayes' theorem updates a belief in light of new evidence:

`P(A|B) = P(B|A) * P(A) / P(B)`

`P(A)` is the prior — what you believed before seeing the evidence. `P(A|B)` is the posterior — the updated belief after seeing evidence `B`. `P(B|A)` is the likelihood — how probable the evidence is if `A` is true.

```python
# Spam filter: does the word "free" make an email more likely to be spam?
p_spam = 0.3                 # prior: 30% of emails are spam
p_free_given_spam = 0.6      # 60% of spam emails contain "free"
p_free_given_not_spam = 0.05 # 5% of legitimate emails contain "free"

p_not_spam = 1 - p_spam
p_free = p_free_given_spam * p_spam + p_free_given_not_spam * p_not_spam   # 0.215
p_spam_given_free = (p_free_given_spam * p_spam) / p_free

print(p_spam_given_free)   # 0.837 — seeing "free" pushes spam probability from 30% to 84%
```

In ML: Naive Bayes classifiers apply this formula directly. More broadly, MLE (above) is the special case of Bayesian inference where you ignore the prior entirely and only maximize the likelihood term `P(data | θ)` — a full Bayesian approach instead keeps a prior over θ and computes a posterior.

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
print(probs)           # [0.63, 0.23, 0.14]
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

### The gradient of softmax + cross-entropy — the elegant shortcut

Cross-entropy is almost always applied directly to softmax's output. Individually, softmax's derivative and log's derivative are both messy — but chained together for this specific pairing, nearly everything cancels, leaving one of the simplest gradients in ML:

`dL/dlogits = (probs - y_true_onehot) / n`

(n = batch size, for the mean loss.) `logits` here means the raw scores *before* softmax — this gradient skips straight past softmax's own Jacobian entirely. This is the very first gradient computed in backprop for any classifier: every other gradient (each layer's `dW`, `db`) chains backward starting from this one.

```python
logits = np.array([[2.0, 1.0, 0.5], [0.1, 0.2, 3.0]])
y_true = np.array([[1, 0, 0], [0, 0, 1]])
n = logits.shape[0]

probs = softmax(logits)
d_logits = (probs - y_true) / n

# Verify against a finite-difference numerical gradient
eps = 1e-6
num_grad = np.zeros_like(logits)
for i in range(logits.shape[0]):
    for j in range(logits.shape[1]):
        logits[i, j] += eps
        loss_plus = cross_entropy(y_true, softmax(logits))
        logits[i, j] -= 2 * eps
        loss_minus = cross_entropy(y_true, softmax(logits))
        logits[i, j] += eps
        num_grad[i, j] = (loss_plus - loss_minus) / (2 * eps)

print(np.allclose(d_logits, num_grad, atol=1e-6))   # True
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

*Last updated: 2026-09-01*
