# NumPy Exercises — Phase 0 Proficiency
## 2–3 days of focused practice | ~60 exercises

---

> **How to use this document:** Work through sections in order. Each section builds on the previous. You have already done slicing, broadcasting, and basic ufuncs — so this starts from where you are and pushes into the things you have not yet drilled. Do every exercise in a Jupyter notebook. Write the expected output as a comment **before** running it. If your prediction is wrong, understand why before moving on.

> **The rule:** never run first and check. Always predict the output shape and value, write it as a comment, then run. This is the habit that actually builds understanding.

---

> **Note:** projects live in `docs/phase0/projects.md`, not in this file.

---

# SECTION 1 — Array Creation and dtypes
*Skills: constructors, dtype awareness, memory layout*

**These are warm-up. They should take 10–15 minutes total.**

---

**Exercise 1.1** — Create the following arrays and print their `.shape`, `.dtype`, `.ndim`, and `.size` for each. Before running, write down what you expect for all four attributes.

```
a) A 1D array of integers from 0 to 9
b) A 2D array of zeros with shape (4, 7)
c) A 3D array of ones with shape (2, 3, 5)
d) A 4x4 identity matrix
e) 10 evenly spaced floats between 0 and 1 (inclusive)
f) Integers from 10 down to 0 (inclusive), step -2
g) A 3x3 array filled with the value 99.0
```

Expected outcomes: you should be able to predict every attribute before running.

---

**Exercise 1.2** — dtype arithmetic. Predict the dtype of each result, then verify.

```python
a = np.array([1, 2, 3])             # dtype?
b = np.array([1.0, 2.0, 3.0])       # dtype?
c = np.array([1, 2, 3], dtype=np.float32)  # dtype?
d = a + b                            # dtype? (mixing int64 and float64)
e = a + c                            # dtype? (mixing int64 and float32)
f = np.array([True, False, True])    # dtype?
g = f.astype(np.int32)               # dtype?
h = np.array([1, 2, 3]).astype(np.float32)  # dtype?
```

The rule you must internalize: NumPy always upcasts to the more precise type.

---

**Exercise 1.3** — Random arrays with reproducibility.

Create the following and verify they are identical when run twice:
```python
np.random.seed(42)
a = np.random.randn(3, 4)
b = np.random.randint(0, 100, size=(5, 5))
c = np.random.uniform(low=-1.0, high=1.0, size=(2, 3))
```
Then: without resetting the seed, create another array. Show that this one differs each run. Explain in a comment why seed resets matter for reproducibility.

---

**Exercise 1.4** — nbytes and memory.

Create these two arrays and compare their memory usage:
```python
a = np.random.randn(1000, 1000)           # float64
b = np.random.randn(1000, 1000).astype(np.float32)  # float32
```
Compute: `a.nbytes`, `b.nbytes`. Calculate the ratio. Explain in a comment why this matters for GPU training.

---

# SECTION 2 — Indexing: Advanced Patterns
*You already know basic slicing. This section drills fancy indexing, multi-dimensional indexing, and the patterns you will use in ML constantly.*

---

**Exercise 2.1** — Multi-dimensional indexing practice. Work through each line and predict the output shape and values before running.

```python
a = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12],
              [13, 14, 15, 16]])   # shape (4, 4)

# Predict shape and values for each:
print(a[1, :])          # ?
print(a[:, 2])          # ?
print(a[1:3, 1:3])      # ?
print(a[::2, ::2])      # ?    (every other row, every other column)
print(a[-1, :])         # ?
print(a[:, -2:])        # ?
print(a[0:3:2, 1:4:2])  # ?    (think carefully about this one)
```

---

**Exercise 2.2** — Boolean indexing is used everywhere in data cleaning. All without loops.

Given:
```python
np.random.seed(0)
X = np.random.randn(100, 5)   # 100 data samples, 5 features
```

Do all of the following without any Python loop:
```
a) Extract all rows where the first feature (column 0) is positive
b) Extract all rows where the absolute value of column 2 is greater than 1.5
c) Count how many rows have ALL features greater than 0
d) Set every value in X that is greater than 2.0 to exactly 2.0 (clipping)
   — then verify by checking that X.max() == 2.0
e) Create a boolean mask of shape (100, 5) that is True wherever X is in the range (-0.5, 0.5)
f) Count True values in each column of that mask
```

For each, write the expected result type (scalar, 1D array, 2D array, etc.) as a comment before writing the code.

---

**Exercise 2.3** — Fancy indexing. This is the pattern used to implement batching and data sampling.

```python
np.random.seed(7)
data = np.random.randn(50, 4)   # 50 samples, 4 features
labels = np.random.randint(0, 3, size=50)   # class 0, 1, or 2
```

Tasks:
```
a) Select rows at indices [0, 7, 13, 42] — what shape is the result?
b) Select rows where label is class 1 — how many rows?
c) Randomly sample 10 rows WITHOUT replacement using np.random.choice
   and np.random.permutation. What is the shape of the result?
d) Select the samples from class 0 and class 2 combined (not class 1)
e) Create a new array where the rows are sorted by the value in column 3
   (use np.argsort). Do not use Python sort.
```

---

**Exercise 2.4** — Views vs copies — understanding it deeply.

This is one of the most important topics. Work through each case and predict whether the original array changes.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)

# Case 1: slice, then modify
b = a[0:2, 0:2]
b[0, 0] = 999
print(a[0, 0])   # changed or not?

# Case 2: boolean index, then modify
c = a[a > 5]
c[0] = 999
print(a)   # changed or not?

# Case 3: fancy index, then modify
d = a[[0, 1], :]
d[0, 0] = 777
print(a[0, 0])   # changed or not?

# Case 4: copy, then modify
e = a[0:2, 0:2].copy()
e[0, 0] = 555
print(a[0, 0])   # changed or not?

# Case 5: reshape
f = a.reshape(9)
f[0] = 111
print(a[0, 0])   # changed or not?

# Case 6: transpose
g = a.T
g[0, 0] = 222
print(a[0, 0])   # changed or not?
```

Write the rule you extract from this as a comment: which operations produce views, which produce copies?

---

# SECTION 3 — Broadcasting: Deep Drills
*You have done basic broadcasting. These exercises target the edge cases and the patterns that appear in ML code.*

---

**Exercise 3.1** — Shape prediction. For each pair of shapes, write:
- Valid or Error
- If valid: what is the output shape?
- Which rule is being applied?

Do this on paper first, then verify in NumPy.

```
(3,)       + (3,)        → ?
(1, 3)     + (3, 1)      → ?
(4, 3)     + (3,)        → ?
(4, 3)     + (4, 1)      → ?
(4, 3)     + (1,)        → ?
(2, 4, 3)  + (4, 3)      → ?
(2, 4, 3)  + (3,)        → ?
(2, 4, 3)  + (4, 1)      → ?
(2, 4, 3)  + (2, 1, 3)   → ?
(3, 1)     + (1, 4)      → ?
(5, 3)     + (3, 5)      → Error? or valid?
(1, 1, 4)  + (3, 1, 1)   → ?
```

For each valid one, create actual arrays of those shapes and verify the result shape.

---

**Exercise 3.2** — Outer operations using broadcasting. These patterns appear constantly in distance computations and attention scores.

```python
a = np.array([1, 2, 3, 4])      # shape (4,)
b = np.array([10, 20, 30])      # shape (3,)
```

Without any loops:
```
a) Compute the outer sum: result[i, j] = a[i] + b[j]
   Expected shape: (4, 3)
   Expected first row: [11, 21, 31]
   Expected first column: [11, 12, 13, 14]

b) Compute the outer product: result[i, j] = a[i] * b[j]
   Expected shape: (4, 3)

c) For each pair (a[i], b[j]), compute a[i] / (a[i] + b[j])
   Expected shape: (4, 3)
```

You will need to reshape `a` to `(4, 1)` or `b` to `(1, 3)`.

---

**Exercise 3.3** — Pairwise Euclidean distances. This is a fundamental ML operation used in k-NN, k-means, and similarity search. You must implement it with no loops.

Given two sets of points:
```python
np.random.seed(1)
A = np.random.randn(5, 3)    # 5 points in 3D space
B = np.random.randn(8, 3)    # 8 points in 3D space
```

Compute a distance matrix `D` of shape `(5, 8)` where `D[i, j]` is the Euclidean distance between `A[i]` and `B[j]`.

Euclidean distance: `d(a, b) = sqrt(sum((a_k - b_k)^2))`

**Approach — think about the shapes step by step:**
- You need `A[i] - B[j]` for all pairs. What shapes do A and B need to be?
- A needs to become shape `(5, 1, 3)` and B needs to become `(1, 8, 3)`
- Their difference broadcasts to `(5, 8, 3)`
- Then square, sum along the last axis, take sqrt

Verification: the distance from any point to itself should be 0. Check this for A vs A.

---

**Exercise 3.4** — Feature normalization using broadcasting. This is what StandardScaler does internally.

```python
np.random.seed(42)
X = np.random.randn(1000, 8) * np.array([1, 5, 0.1, 100, 2, 50, 0.5, 10])
# Each column has very different scale
```

Without loops:
```
a) Compute the mean of each column. Shape: (8,)
b) Compute the std of each column. Shape: (8,)
c) Standardize X: subtract each column's mean, divide by each column's std
   Call the result X_norm. Shape: (1000, 8)
d) Verify: X_norm.mean(axis=0) should be all ~0
           X_norm.std(axis=0) should be all ~1
e) Now compute min-max normalization instead: for each column, subtract
   that column's min and divide by (max - min), so every value lands in [0, 1]
   Verify: each column should be in range [0, 1]
```

---

**Exercise 3.5** — Batch operations. This is how neural networks process data in parallel.

```python
# A "batch" of 32 samples, each with 16 features
np.random.seed(5)
batch = np.random.randn(32, 16)

# A weight matrix: transforms 16 features to 8 outputs
W = np.random.randn(16, 8)
b = np.random.randn(8)          # bias, one per output
```

```
a) Compute the linear transformation: output = batch @ W + b
   What is the output shape? Predict before computing.

b) Apply ReLU to the output: max(0, x) element-wise
   Use np.maximum, not a loop.
   What fraction of values are exactly 0.0?

c) Now assume you have a BATCH of weight matrices — one per sample:
   W_batch = np.random.randn(32, 16, 8)
   How do you compute batch_i @ W_batch_i for each sample i simultaneously?
   Hint: this requires np.einsum or a reshape trick.
   Expected output shape: (32, 8)
```

---

# SECTION 4 — Aggregation and Shape Manipulation
*The axis parameter, reduce operations, reshape, stack — these trip people up until they become automatic.*

---

**Exercise 4.1** — The axis parameter. Master it here.

```python
X = np.arange(24).reshape(2, 3, 4)
# Shape (2, 3, 4) — think of it as 2 "blocks", each 3x4

# For each operation, predict the output shape and value before running:
print(X.sum())              # ?  (scalar)
print(X.sum(axis=0))        # shape?
print(X.sum(axis=1))        # shape?
print(X.sum(axis=2))        # shape?
print(X.sum(axis=(0, 1)))   # shape?
print(X.sum(axis=(1, 2)))   # shape?
print(X.mean(axis=0))       # shape?
print(X.max(axis=2))        # shape?
print(X.argmax(axis=2))     # shape? what does this mean?
```

After getting these right, state the rule in plain language in a comment: "When I use axis=k, the result loses dimension k because..."

---

**Exercise 4.2** — keepdims. This is crucial for writing broadcasting-compatible code.

```python
X = np.random.randn(100, 5)

# Version 1 — without keepdims
mean = X.mean(axis=0)      # shape (5,)
X_centered = X - mean       # works? what shapes?

# Version 2 — with keepdims
mean_k = X.mean(axis=0, keepdims=True)  # shape?
X_centered_k = X - mean_k               # works? what shapes?

# Now try on axis=1
row_sum = X.sum(axis=1)             # shape?
row_sum_k = X.sum(axis=1, keepdims=True)  # shape?

# Which version lets you do X / row_sum without errors?
# Try both and understand why one fails.
```

Then implement softmax using keepdims correctly:
```python
def softmax(logits):
    # logits shape: (n_samples, n_classes)
    # Your implementation — must work for batched inputs
    # Must use keepdims to subtract max correctly
    pass

# Test:
logits = np.array([[1.0, 2.0, 3.0],
                   [4.0, 1.0, 2.0]])
result = softmax(logits)
print(result.sum(axis=1))   # should be [1.0, 1.0]
```

---

**Exercise 4.3** — reshape: know exactly what it does.

```python
a = np.arange(24)

# Predict the shape and content of the first row for each:
b = a.reshape(4, 6)         # first row of b?
c = a.reshape(6, 4)         # first row of c?
d = a.reshape(2, 3, 4)      # d[0]?  d[0, 0]?
e = a.reshape(2, -1)        # shape?
f = a.reshape(-1, 8)        # shape?

# Critical question: does reshape return a view or copy usually?
g = a.reshape(4, 6)
g[0, 0] = 999
print(a[0])   # changed?
```

Now implement flatten and ravel:
```python
M = np.random.randn(3, 4, 5)
flat_1 = M.flatten()    # shape? view or copy?
flat_2 = M.ravel()      # shape? view or copy?

# How do you verify which is a view and which is a copy?
flat_2[0] = 9999
print(M[0, 0, 0])       # changed?
```

---

**Exercise 4.4** — Adding and removing dimensions. This is used constantly when preparing inputs for ML operations.

```python
v = np.array([1.0, 2.0, 3.0, 4.0, 5.0])   # shape (5,)

# Create all of these from v:
row_vector  = ?    # shape (1, 5)
col_vector  = ?    # shape (5, 1)
tensor_3d   = ?    # shape (1, 5, 1)
# Use np.newaxis, reshape, and expand_dims — try all three approaches

# Squeeze:
x = np.random.randn(1, 5, 1, 3, 1)
print(x.shape)
print(np.squeeze(x).shape)           # removes all size-1 dims
print(np.squeeze(x, axis=0).shape)   # removes only axis 0
print(np.squeeze(x, axis=2).shape)   # removes only axis 2
```

Now a practical exercise — compute the outer product of two vectors using broadcasting and dimension insertion:
```python
a = np.array([1, 2, 3])    # shape (3,)
b = np.array([10, 20])     # shape (2,)

# Compute outer product: result[i, j] = a[i] * b[j]
# Shape should be (3, 2)
# Do it using only reshape/newaxis — no np.outer
```

---

**Exercise 4.5** — Stack and concatenate. These are used in data pipeline construction.

```python
arrays = [np.random.randn(10, 5) for _ in range(4)]

# Concatenate along axis 0 (stack rows):
result_0 = np.concatenate(arrays, axis=0)    # shape?

# Concatenate along axis 1 (stack columns):
result_1 = np.concatenate(arrays, axis=1)    # shape?

# np.stack creates a NEW dimension:
stacked = np.stack(arrays, axis=0)    # shape?
stacked_1 = np.stack(arrays, axis=1) # shape?

# vstack and hstack:
a = np.array([[1, 2], [3, 4]])   # shape (2, 2)
b = np.array([[5, 6], [7, 8]])   # shape (2, 2)
print(np.vstack([a, b]).shape)    # ?
print(np.hstack([a, b]).shape)    # ?
```

Practical task: you have a list of 8 images, each represented as an array of shape `(32, 32, 3)`. Stack them into a single batch tensor of shape `(8, 32, 32, 3)` using one line of NumPy code.

---

# SECTION 5 — Linear Algebra
*This is where NumPy connects directly to ML math. Every operation here appears in neural networks.*

---

**Exercise 5.1** — Matrix multiply: understand what it computes.

For each product, predict the output shape. Then compute the first element of the result by hand (just C[0,0]) and verify.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])          # shape (2, 3)

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])            # shape (3, 2)

C = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])          # shape (3, 3) — identity

v = np.array([1, 2, 3])           # shape (3,)
```

Compute and predict shapes:
```
A @ B          → shape?   C[0,0] by hand?
A @ C          → shape?
C @ A.T        → shape?
v @ A.T        → shape?    (what does this compute?)
A.T @ A        → shape?    (this matrix has a special name — what is it?)
np.outer(v, v) → shape?
```

---

**Exercise 5.2** — The neural network forward pass as matrix operations.

```python
np.random.seed(42)

# A batch of 64 samples, 128 features
X = np.random.randn(64, 128)

# Layer 1: 128 → 64 neurons
W1 = np.random.randn(128, 64) * 0.01
b1 = np.zeros(64)

# Layer 2: 64 → 32 neurons
W2 = np.random.randn(64, 32) * 0.01
b2 = np.zeros(32)

# Layer 3: 32 → 10 outputs (10 classes)
W3 = np.random.randn(32, 10) * 0.01
b3 = np.zeros(10)
```

Implement the full forward pass:
```
a) Z1 = X @ W1 + b1        — shape?
b) A1 = relu(Z1)            — shape? (ReLU = max(0, x))
c) Z2 = A1 @ W2 + b2       — shape?
d) A2 = relu(Z2)            — shape?
e) Z3 = A2 @ W3 + b3       — shape?
f) probs = softmax(Z3)      — shape?
g) Verify: probs.sum(axis=1) ≈ 1.0 for all 64 samples
```

Before writing any code, write out all intermediate shapes on paper. This is the exact pattern you will use in Phase 2.

---

**Exercise 5.3** — Solving linear systems.

```python
# You have a system of equations: Ax = b
A = np.array([[3, 1, -2],
              [2, -4, 1],
              [1, 2, 3]], dtype=float)

b = np.array([5, -1, 10], dtype=float)
```

```
a) Solve using np.linalg.solve(A, b) — this is more stable than computing A_inv @ b
b) Verify: A @ solution should equal b (use np.allclose)
c) Solve using A_inv = np.linalg.inv(A); solution = A_inv @ b
d) Are the two solutions identical? Use np.allclose to check.
e) Why is np.linalg.solve preferred over computing the inverse?
   (Hint: think about numerical stability and the number of operations)
```

---

**Exercise 5.4** — Norms and distances.

```python
np.random.seed(3)
v1 = np.random.randn(100)
v2 = np.random.randn(100)
M = np.random.randn(5, 8)
```

```
a) L2 norm of v1           → one line
b) L1 norm of v1           → one line
c) Euclidean distance between v1 and v2 → one line (using norm)
d) Cosine similarity between v1 and v2:
   cos_sim = (v1 · v2) / (||v1|| * ||v2||)
   Result should be in range [-1, 1]
e) Frobenius norm of M     → one line
f) L2 norm of each row of M (should give 5 values) — one line, no loop
   Hint: use axis parameter
```

---

**Exercise 5.5** — Eigendecomposition and its meaning.

```python
# Create a symmetric matrix (its eigenvalues will be real)
np.random.seed(42)
A = np.random.randn(4, 4)
M = A.T @ A    # symmetric, positive semi-definite
```

```
a) Compute eigenvalues and eigenvectors of M
b) Verify the eigenvalue equation: M @ v ≈ λ * v for each eigenvector
   (Check all 4 eigenvectors in a loop — this is fine, it's verification not computation)
c) Sort eigenvalues from largest to smallest
d) The largest eigenvalue corresponds to the direction of greatest variance.
   Verify: np.linalg.norm(M @ eigenvectors[:, 0]) is larger than
           np.linalg.norm(M @ eigenvectors[:, -1])
e) Reconstruct M from its eigendecomposition:
   M ≈ eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T
   Verify with np.allclose
```

---

**Exercise 5.6** — SVD: the most important decomposition in ML.

```python
np.random.seed(7)
M = np.random.randn(6, 4)    # 6 rows, 4 columns
```

```
a) Compute SVD: U, S, Vt = np.linalg.svd(M, full_matrices=False)
b) Print shapes of U, S, Vt — explain what each represents
c) Reconstruct M: M_reconstructed = U @ np.diag(S) @ Vt
   Verify with np.allclose
d) Low-rank approximation — keep only top 2 singular values:
   M_approx = U[:, :2] @ np.diag(S[:2]) @ Vt[:2, :]
   Compute the approximation error: np.linalg.norm(M - M_approx, ord='fro')
e) Keep only top 1 singular value. What is the error now?
f) What percentage of the total "energy" (sum of squared singular values)
   is captured by the top 1 and top 2 components?
   energy_ratio = S[:k]**2 / (S**2).sum()
```

This is exactly how LoRA works — representing weight updates as low-rank products U @ Vt.

---

**Exercise 5.7** — Covariance matrix and PCA from scratch.

```python
np.random.seed(0)
# Create correlated data: feature 2 is roughly 3 * feature 1 + noise
n = 200
x1 = np.random.randn(n)
x2 = 3 * x1 + 0.5 * np.random.randn(n)
x3 = np.random.randn(n)   # independent of x1 and x2
X = np.column_stack([x1, x2, x3])   # shape (200, 3)
```

Implement PCA from scratch using only NumPy:
```
Step 1: Center the data (subtract column means)
Step 2: Compute the covariance matrix using np.cov(X_centered.T)
        Shape should be (3, 3)
Step 3: Compute eigenvalues and eigenvectors of the covariance matrix
Step 4: Sort eigenvalues descending, reorder eigenvectors accordingly
Step 5: Project X_centered onto the top 2 principal components
        X_2d = X_centered @ top_2_eigenvectors
        Shape should be (200, 2)
Step 6: Verify that X_2d[:, 0].var() > X_2d[:, 1].var()
        (first PC captures more variance than second)
Step 7: Print the explained variance ratio for each component:
        explained[k] = eigenvalue[k] / sum(eigenvalues)
```

Expected: the first component should capture ~90%+ of the variance since x1 and x2 are strongly correlated.

---

# SECTION 6 — einsum
*You need to know this well enough to read and write transformer code.*

---

**Exercise 6.1** — Basic einsum notation.

Rewrite each operation using einsum:
```python
a = np.random.randn(3)
b = np.random.randn(3)
A = np.random.randn(3, 4)
B = np.random.randn(4, 5)
C = np.random.randn(3, 4, 5)
D = np.random.randn(3, 4, 5)

# Write the einsum equivalent for each:
np.dot(a, b)                   # → np.einsum(?, a, b)
a[:, np.newaxis] * b           # → np.einsum(?, a, b)  [outer product]
A @ B                          # → np.einsum(?, A, B)
A.T                            # → np.einsum(?, A)
A.sum(axis=0)                  # → np.einsum(?, A)
A.sum(axis=1)                  # → np.einsum(?, A)
(A * A).sum()                  # → np.einsum(?, A)      [sum of squares]
np.diag(A @ A.T)               # → np.einsum(?, A, A)   [diagonal of gram matrix]
```

For each, verify the result matches the non-einsum version.

---

**Exercise 6.2** — Batch operations with einsum.

```python
# A batch of 8 matrices, each 3x4
batch_A = np.random.randn(8, 3, 4)
# A batch of 8 matrices, each 4x5
batch_B = np.random.randn(8, 4, 5)

# A single shared weight vector of length 4
w = np.random.randn(4)
```

```
a) Batch matrix multiply: for each of the 8 pairs, compute A[i] @ B[i]
   Result shape: (8, 3, 5)
   Write with einsum (hint: the batch index "b" appears unchanged on both
   sides — it's the middle index that gets summed over, same as a normal matmul)
   Verify against: np.stack([batch_A[i] @ batch_B[i] for i in range(8)])

b) For each of the 8 matrices in batch_A, compute the dot product of each row with w
   Result shape: (8, 3)
   Write with einsum.

c) For each of the 8 matrices in batch_A, compute A[i].T @ A[i]  (3x3 gram matrix)
   Result shape: (8, 4, 4)
   Write with einsum.
```

---

**Exercise 6.3** — Attention scores with einsum. This is used in transformers.

```python
np.random.seed(42)
batch_size = 2
seq_len = 5
d_k = 8    # dimension of keys/queries

Q = np.random.randn(batch_size, seq_len, d_k)    # queries
K = np.random.randn(batch_size, seq_len, d_k)    # keys
V = np.random.randn(batch_size, seq_len, d_k)    # values
```

Implement scaled dot-product attention:
```
Step 1: Compute raw attention scores — conceptually this is Q @ K.T per
        batch, so write the batched version yourself with einsum.
        Shape: (batch_size, seq_len, seq_len)
        (hint: "b" stays on both sides unchanged; the "d" dimension — the
        one shared by Q and K — is what gets summed away)

Step 2: Scale by sqrt(d_k)
        scores = scores / np.sqrt(d_k)

Step 3: Apply softmax along the last axis (axis=-1)
        attention_weights = softmax(scores)
        Each row of each attention matrix should sum to 1.0

Step 4: Weighted sum of values — combine attention_weights and V with einsum.
        Shape: (batch_size, seq_len, d_k)
        (hint: the key-position axis is what's being summed over here — it
        shows up in both attention_weights and V, but not in the output)

Step 5: Verify attention_weights.sum(axis=-1) ≈ 1.0 everywhere
```

This is the exact computation inside a transformer's self-attention mechanism.

---

# SECTION 7 — Numerical Stability and Common Pitfalls
*These are the bugs you will hit in real ML code.*

---

**Exercise 7.1** — Float comparison: why == is wrong.

```python
# These should all be True mathematically. Check which ones are:
print(0.1 + 0.2 == 0.3)
print(np.float32(0.1) + np.float32(0.2) == np.float32(0.3))
print(np.sin(np.pi) == 0.0)
print(np.sum(np.ones(10) * 0.1) == 1.0)
```

For each False result: use `np.isclose` with appropriate tolerance instead. Write the rule: "Never use == to compare floating point numbers. Instead use..."

---

**Exercise 7.2** — Integer overflow. Understand why dtype matters for computation.

```python
a = np.array([200, 200, 200], dtype=np.int8)   # int8 range: -128 to 127
print(a.sum())    # What happens?

b = np.array([200, 200, 200], dtype=np.int32)
print(b.sum())    # What happens now?

c = np.array([1000, 1000, 1000], dtype=np.int16)  # int16 range: -32768 to 32767
print(c.sum())    # Overflow?
```

Then fix each by casting to an appropriate dtype before summing.

---

**Exercise 7.3** — log(0) and division by zero.

```python
# These are real bugs in ML code
probs = np.array([0.5, 0.3, 0.2, 0.0])   # last prob is 0 — can happen

# Problem 1: log of zero
log_probs = np.log(probs)   # what is log(0)?

# Fix: add a small epsilon so log() never sees exactly 0
eps = 1e-9
log_probs_safe = ...

# Problem 2: division by zero
counts = np.array([10, 5, 0, 3])
ratios = probs / counts   # what happens at index 2?

# Fix: avoid ever dividing by exact zero
# (hint: np.where(condition, value_if_true, value_if_false) lets you swap
# in a safe value only where counts == 0, instead of dividing by it)
safe_ratios = ...
```

Also implement a numerically stable log-sum-exp:
```python
def log_sum_exp(x):
    """Numerically stable log(sum(exp(x))) for a 1D array."""
    # Naive: np.log(np.sum(np.exp(x)))
    # Problem: exp(large_number) overflows to inf
    # Fix: subtract the max first
    # log(sum(exp(x))) = max(x) + log(sum(exp(x - max(x))))
    pass

# Test:
x = np.array([1000.0, 1001.0, 1002.0])
print(log_sum_exp(x))   # should NOT be inf
print(np.log(np.sum(np.exp(x))))   # this overflows
```

---

**Exercise 7.4** — The (n,) vs (n,1) vs (1,n) trap.

This causes bugs in almost every ML project. Go through all cases carefully.

```python
a = np.array([1, 2, 3])      # shape (3,)
b = a.reshape(3, 1)           # shape (3, 1)
c = a.reshape(1, 3)           # shape (1, 3)

M = np.random.randn(3, 3)

# For each operation, predict: will it work? What shape is the result?
print((M @ a).shape)     # M(3x3) @ a(3,) → ?
print((M @ b).shape)     # M(3x3) @ b(3,1) → ?
print((a @ M).shape)     # a(3,) @ M(3x3) → ?
print((b.T @ M).shape)   # b.T(1x3) @ M(3x3) → ?

# Broadcasting with different shapes:
print((a + a).shape)     # (3,) + (3,) → ?
print((a + b).shape)     # (3,) + (3,1) → ?    ← dangerous
print((a + c).shape)     # (3,) + (1,3) → ?    ← fine but (3,3)
print((b + c).shape)     # (3,1) + (1,3) → ?   ← (3,3) outer sum
```

Write a summary: "When should I use shape (n,) vs (n,1)?"

---

# SECTION 8 — ML-Specific Patterns
*The exact NumPy patterns that appear in the neural networks you will build.*

---

**Exercise 8.1** — Implement all ML activation functions from scratch. All must be vectorized (no loops).

```python
def relu(x: np.ndarray) -> np.ndarray:
    """max(0, x) element-wise"""
    pass

def leaky_relu(x: np.ndarray, alpha: float = 0.01) -> np.ndarray:
    """x if x > 0 else alpha*x"""
    pass

def sigmoid(x: np.ndarray) -> np.ndarray:
    """1 / (1 + exp(-x))"""
    # Numerically stable: handle positive and negative separately
    pass

def tanh(x: np.ndarray) -> np.ndarray:
    """(exp(x) - exp(-x)) / (exp(x) + exp(-x))"""
    # Use np.tanh — just make sure you know the formula
    pass

def softmax(x: np.ndarray) -> np.ndarray:
    """exp(x) / sum(exp(x)), stable version, works on 2D batches"""
    # Must handle input of shape (n_samples, n_classes)
    # Must subtract max for stability
    pass

def gelu(x: np.ndarray) -> np.ndarray:
    """x * Phi(x) where Phi is standard normal CDF"""
    # Approximation: 0.5 * x * (1 + np.tanh(sqrt(2/pi) * (x + 0.044715 * x**3)))
    pass
```

Test suite — all must pass:
```python
x = np.array([-3, -1, 0, 1, 3], dtype=float)

assert np.all(relu(x) >= 0), "ReLU: all outputs >= 0"
assert relu(np.array([0.0]))[0] == 0.0
assert relu(np.array([5.0]))[0] == 5.0

assert np.all((sigmoid(x) > 0) & (sigmoid(x) < 1)), "Sigmoid range (0,1)"
assert np.isclose(sigmoid(np.array([0.0]))[0], 0.5)

assert np.all((tanh(x) > -1) & (tanh(x) < 1)), "Tanh range (-1,1)"
assert np.isclose(tanh(np.array([0.0]))[0], 0.0)

batch = np.array([[1.0, 2.0, 3.0], [4.0, 1.0, 2.0]])
sm = softmax(batch)
assert sm.shape == (2, 3), "Softmax shape"
assert np.allclose(sm.sum(axis=1), [1.0, 1.0]), "Softmax sums to 1"
assert np.all(sm > 0), "Softmax positive"
```

---

**Exercise 8.2** — Loss functions from scratch.

```python
def mse_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """Mean squared error: mean((y_pred - y_true)^2)"""
    pass

def mae_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """Mean absolute error: mean(|y_pred - y_true|)"""
    pass

def binary_cross_entropy(y_pred_prob: np.ndarray, y_true: np.ndarray) -> float:
    """
    Binary cross-entropy.
    y_pred_prob: predicted probabilities, shape (n,), values in (0, 1)
    y_true: binary labels, shape (n,), values 0 or 1
    """
    pass

def categorical_cross_entropy(y_pred_probs: np.ndarray, y_true_onehot: np.ndarray) -> float:
    """
    Multi-class cross-entropy.
    y_pred_probs: softmax output, shape (n, k)
    y_true_onehot: one-hot labels, shape (n, k)
    """
    pass

def cross_entropy_from_logits(logits: np.ndarray, y_true_labels: np.ndarray) -> float:
    """
    Cross-entropy directly from raw logits (more stable than softmax then log).
    logits: shape (n, k) — raw model output
    y_true_labels: shape (n,) — integer class indices
    
    Hint: log(softmax(logits))_correct_class = logits_correct - log(sum(exp(logits)))
    Use the log-sum-exp trick for stability.
    """
    pass
```

Test suite:
```python
y_true_r = np.array([1.0, 2.0, 3.0, 4.0])
y_pred_r = np.array([1.1, 1.9, 3.2, 3.8])

assert np.isclose(mse_loss(y_pred_r, y_true_r), np.mean((y_pred_r - y_true_r)**2))
assert np.isclose(mae_loss(y_pred_r, y_true_r), np.mean(np.abs(y_pred_r - y_true_r)))

y_true_b = np.array([1, 0, 1, 1, 0], dtype=float)
y_pred_b = np.array([0.9, 0.1, 0.8, 0.7, 0.3])
bce = binary_cross_entropy(y_pred_b, y_true_b)
assert bce > 0, "BCE must be positive"
assert bce < 1.0, "BCE should be small for good predictions"

# Good predictions should have lower loss than bad
logits_good = np.array([[5.0, 0.0, 0.0], [0.0, 5.0, 0.0]])   # very confident correct
logits_bad  = np.array([[0.0, 5.0, 0.0], [5.0, 0.0, 0.0]])   # very confident wrong
labels = np.array([0, 1])
assert cross_entropy_from_logits(logits_good, labels) < cross_entropy_from_logits(logits_bad, labels)
```

---

**Exercise 8.3** — Gradient implementations. You computed these by hand in Phase 0 theory. Now implement them as vectorized NumPy functions.

```python
def mse_gradient(y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
    """
    Gradient of MSE w.r.t. y_pred.
    d(MSE)/d(y_pred) = 2/n * (y_pred - y_true)
    Shape: same as y_pred
    """
    pass

def relu_gradient(x: np.ndarray) -> np.ndarray:
    """
    Gradient of ReLU w.r.t. its input.
    1 where x > 0, 0 where x <= 0.
    Shape: same as x
    """
    pass

def linear_layer_gradients(d_out: np.ndarray, x: np.ndarray, W: np.ndarray):
    """
    Gradients for y = x @ W + b.
    d_out: gradient flowing backward from next layer, shape (n, out)
    x: input to this layer, shape (n, in)
    W: weight matrix, shape (in, out)
    
    Returns: (d_x, d_W, d_b)
    d_x = d_out @ W.T          shape (n, in)
    d_W = x.T @ d_out          shape (in, out)
    d_b = d_out.sum(axis=0)    shape (out,)
    """
    pass
```

Verify the linear layer gradients using numerical gradient checking:
```python
def numerical_gradient(loss_fn, param, eps=1e-5):
    """Compute gradient numerically using finite differences."""
    grad = np.zeros_like(param)
    it = np.nditer(param, flags=["multi_index"])
    while not it.finished:
        idx = it.multi_index
        original = param[idx]
        param[idx] = original + eps
        f_plus = loss_fn()
        param[idx] = original - eps
        f_minus = loss_fn()
        grad[idx] = (f_plus - f_minus) / (2 * eps)
        param[idx] = original
        it.iternext()
    return grad

# Test:
np.random.seed(42)
x = np.random.randn(4, 3)
W = np.random.randn(3, 5)
b = np.random.randn(5)
y_true = np.random.randn(4, 5)

def loss():
    y_pred = x @ W + b
    return np.mean((y_pred - y_true)**2)

def analytical_dW():
    y_pred = x @ W + b
    d_out = 2 / (4*5) * (y_pred - y_true)
    _, dW, _ = linear_layer_gradients(d_out, x, W)
    return dW

num_grad = numerical_gradient(loss, W.copy())
anal_grad = analytical_dW()
print(np.allclose(num_grad, anal_grad, atol=1e-5))   # should be True
```

---

**Exercise 8.4** — Implement k-means clustering from scratch in NumPy.

This is the Phase 0 checklist item: "Can implement k-means clustering from scratch in NumPy."

```python
def kmeans(X: np.ndarray, k: int, max_iters: int = 100, seed: int = 42) -> tuple:
    """
    k-means clustering implemented in NumPy.
    
    X: data array, shape (n_samples, n_features)
    k: number of clusters
    max_iters: maximum iterations
    seed: random seed for initialization
    
    Returns: (centroids, labels, inertia_history)
    centroids: shape (k, n_features) — final centroid positions
    labels: shape (n_samples,) — cluster assignment for each sample
    inertia_history: list of inertia at each iteration
    
    Algorithm:
    1. Initialize k centroids by randomly selecting k data points
    2. Assignment step: assign each point to its nearest centroid
       (use vectorized distance computation — no loops over points)
    3. Update step: move each centroid to the mean of its assigned points
    4. Repeat 2-3 until assignments don't change or max_iters reached
    5. Compute inertia: sum of squared distances from each point to its centroid
    """
    pass
```

Test it:
```python
# Create well-separated clusters
np.random.seed(0)
cluster1 = np.random.randn(50, 2) + np.array([0, 0])
cluster2 = np.random.randn(50, 2) + np.array([5, 5])
cluster3 = np.random.randn(50, 2) + np.array([10, 0])
X = np.vstack([cluster1, cluster2, cluster3])

centroids, labels, history = kmeans(X, k=3)

# Verify:
print(f"Unique labels: {np.unique(labels)}")          # should be [0, 1, 2]
print(f"Cluster sizes: {np.bincount(labels)}")        # should be ~[50, 50, 50]
print(f"Inertia decreased: {history[0] > history[-1]}")   # should be True

# Visualization (if matplotlib available)
import matplotlib.pyplot as plt
colors = ['red', 'blue', 'green']
for i in range(3):
    mask = labels == i
    plt.scatter(X[mask, 0], X[mask, 1], c=colors[i], alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, linewidths=3)
plt.title("k-Means Clustering Result")
plt.show()
```

---

# COMPLETION CHECKLIST

Work through this after finishing all sections and projects. Be honest.

**Array operations:**
- [ ] Can predict output shape of any operation before running it
- [ ] Knows when slicing returns a view vs a copy — can state the rule
- [ ] Comfortable with boolean and fancy indexing on multi-dimensional arrays
- [ ] Can select rows, columns, and submatrices without confusion

**Broadcasting:**
- [ ] Can work out whether any two shapes broadcast, and what the result shape is, without running code
- [ ] Can compute pairwise distances without any Python loop
- [ ] Can perform batch normalization using broadcasting only

**Shape manipulation:**
- [ ] Can explain what `keepdims=True` does and when it is necessary
- [ ] Can reshape, stack, and concatenate arrays correctly on first attempt
- [ ] Can add and remove dimensions fluently using newaxis, reshape, squeeze

**Linear algebra:**
- [ ] Can implement a neural network forward pass as matrix operations
- [ ] Knows the difference between `@`, `*`, and `np.dot` and when to use each
- [ ] Can implement PCA from scratch using eigendecomposition
- [ ] Can perform low-rank matrix approximation using SVD
- [ ] Can implement batch attention scores using einsum

**ML implementations:**
- [ ] Can implement all activation functions vectorized with no loops
- [ ] Can implement MSE, MAE, binary cross-entropy, and categorical cross-entropy from scratch
- [ ] Can implement the gradient of each loss function
- [ ] Can implement k-means clustering in NumPy
- [ ] Has built and trained a two-layer neural network in NumPy

Projects are tracked separately — see `docs/phase0/projects.md` and `phase0/README.md`.

---

*Last updated: 2026-08-08*
