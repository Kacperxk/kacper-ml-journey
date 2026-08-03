# Phase 0 — NumPy Concepts

Part 2 of the Phase 0 teaching content (concepts, not drills — drills are in
`numpy_exercises.md` in this folder). Originally part of `phase0_complete.md`.

---

# PART 2 — NUMPY

## The Right Mindset

NumPy is not a collection of math functions. It is a different way of thinking about data. The shift: instead of "I have a list and I will loop over it," think "I have an array and I will operate on the whole thing at once."

This matters for two reasons. NumPy operations run in compiled C — they are 10–1000x faster than Python loops. And PyTorch tensors work exactly the same way. Everything you learn here transfers directly.

---

## 2.1 — What is an ndarray?

An `ndarray` (N-dimensional array) is a grid of numbers, all of the same type, with any number of dimensions.

- 1D: a sequence — shape `(5,)`
- 2D: a table with rows and columns — shape `(3, 4)`
- 3D: a stack of tables — shape `(2, 3, 4)`

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.shape)   # (5,)
print(a.ndim)    # 1

b = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])
print(b.shape)   # (3, 4)
print(b.ndim)    # 2

c = np.random.randn(2, 3, 4)
print(c.shape)   # (2, 3, 4)
print(c.ndim)    # 3

# The four attributes to always check when debugging:
print(a.shape)    # dimensions
print(a.dtype)    # data type
print(a.ndim)     # number of dimensions
print(a.size)     # total number of elements
```

**`shape` is the most important attribute.** Print it when something breaks. Most ML bugs are shape mismatches.

### Creating arrays:

```python
np.zeros((3, 4))                          # 3x4 of zeros
np.ones((2, 3))                           # 2x3 of ones
np.eye(4)                                 # 4x4 identity matrix
np.full((3, 3), 7.0)                      # 3x3 filled with 7.0
np.arange(0, 10, 2)                       # [0, 2, 4, 6, 8]
np.linspace(0.0, 1.0, 5)                 # [0.0, 0.25, 0.5, 0.75, 1.0]

np.random.seed(42)                        # ALWAYS set this for reproducibility
np.random.randn(3, 4)                     # 3x4 standard normal
np.random.rand(3, 4)                      # 3x4 uniform [0, 1)
np.random.randint(0, 10, size=(3, 4))    # 3x4 random integers

np.array([1, 2, 3], dtype=np.float32)    # 32-bit float (GPU prefers this)
np.array([1, 2, 3], dtype=np.float64)    # 64-bit float (NumPy default)
```

Why dtype matters: PyTorch uses `float32`. NumPy defaults to `float64`. You will be converting between them, so always know what you have.

---

## 2.2 — Indexing and Slicing

```python
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])   # shape (3, 3)

# Single element: [row, col]
a[0, 0]       # 1
a[1, 2]       # 6
a[-1, -1]     # 9 — negative counts from end

# Slices: [start:end, start:end] — end is EXCLUSIVE
a[0, :]       # [1, 2, 3] — whole first row
a[:, 1]       # [2, 5, 8] — whole second column
a[0:2, 0:2]   # [[1,2],[4,5]] — top-left 2x2

# Boolean indexing
mask = a > 5
a[mask]          # [6, 7, 8, 9] — values where mask is True
a[a > 5] = 0     # set those values to 0 in place
```

### Views vs copies — the most important gotcha:

```python
a = np.array([1, 2, 3, 4, 5])

# Slicing returns a VIEW — shares underlying memory with a
b = a[1:4]
b[0] = 99
print(a)        # [1, 99, 3, 4, 5] — a was changed through b!

# .copy() gives an independent array
c = a[1:4].copy()
c[0] = 0
print(a)        # unchanged
```

Views exist for performance. But they cause confusing bugs. When in doubt, call `.copy()`.

---

## 2.3 — Broadcasting — The Most Important NumPy Concept

Broadcasting lets NumPy operate on arrays of different shapes. It is also exactly how PyTorch tensors work. Misunderstanding this causes hours of debugging.

### The three rules

1. If arrays have different numbers of dimensions, pad the smaller one with 1s on the **left**.
   - shape `(3,)` paired with 2D → becomes `(1, 3)`
   - shape `(3,)` paired with 3D → becomes `(1, 1, 3)`

2. Any dimension of size 1 is **stretched** to match the other array.

3. If two dimensions are not equal and neither is 1 → **error**.

```python
# Scalar + array — simplest case
a = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)
a + 10   # [[11,12,13],[14,15,16]] — scalar stretched to (2, 3)

# (1, 3) + (3, 1) → (3, 3)
row = np.array([[1, 2, 3]])        # shape (1, 3)
col = np.array([[10], [20], [30]]) # shape (3, 1)
row + col
# [[11, 12, 13],
#  [21, 22, 23],
#  [31, 32, 33]]   shape (3, 3)

# (100, 3) + (3,) → (100, 3)
# (3,) becomes (1, 3), then stretched to (100, 3)
X = np.random.randn(100, 3)
mean = np.array([0.5, 1.0, -0.5])   # shape (3,)
X - mean                              # shape (100, 3) — works correctly

# (3, 4) + (3,) → ERROR
# (3,) becomes (1, 3). Last dims: 4 vs 3 — incompatible.
```

**Practice habit:** before every operation with different-shaped arrays, write the shapes on paper and predict the result. Do this until it is automatic.

---

## 2.4 — Vectorization: Think in Arrays

When you catch yourself writing a Python loop over a NumPy array, stop. Ask: "can I do this as an array operation?"

```python
import time
data = np.random.randn(1_000_000)

# Loop — slow Python
start = time.time()
result = [x**2 + 2*x + 1 for x in data]
print(f"Loop: {time.time()-start:.3f}s")       # ~0.3s

# Vectorized — fast C
start = time.time()
result = data**2 + 2*data + 1
print(f"Vectorized: {time.time()-start:.3f}s") # ~0.005s — 60x faster
```

Common vectorized operations:

```python
a = np.array([1.0, 2.0, 3.0, 4.0])

a ** 2                # [1, 4, 9, 16]
np.sqrt(a)            # [1.0, 1.41, 1.73, 2.0]
np.exp(a)             # [e^1, e^2, e^3, e^4]
np.log(a)             # natural logarithm
np.abs(-a)            # [1, 2, 3, 4]
np.maximum(a, 2.5)    # [2.5, 2.5, 3.0, 4.0] — element-wise max (this is ReLU!)
np.clip(a, 1.5, 3.0)  # [1.5, 2.0, 3.0, 3.0] — clamp to range
```

---

## 2.5 — Aggregation and Reduction

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)

# Global — collapse everything to a scalar
a.sum()     # 21
a.mean()    # 3.5
a.max()     # 6
a.std()     # standard deviation

# Along an axis
# axis=0: collapse ROWS → one result per column
# axis=1: collapse COLUMNS → one result per row

a.sum(axis=0)    # [5, 7, 9]   — sum down each column
a.sum(axis=1)    # [6, 15]     — sum across each row
a.mean(axis=0)   # [2.5, 3.5, 4.5]
a.max(axis=1)    # [3, 6]

a.argmax(axis=1) # [2, 2] — column index of max in each row
```

ML use case — normalizing features:

```python
X = np.random.randn(100, 5)    # 100 samples, 5 features
mean = X.mean(axis=0)          # shape (5,) — mean per feature
std = X.std(axis=0)            # shape (5,)
X_norm = (X - mean) / std      # (100,5) - (5,) — broadcasting handles it
# Every feature now has mean≈0, std≈1
```

---

## 2.6 — Shape Manipulation

```python
a = np.arange(12)           # shape (12,)

a.reshape(3, 4)             # (3, 4)
a.reshape(2, 3, 2)          # (2, 3, 2) — 3D
a.reshape(3, -1)            # (3, 4) — NumPy infers the -1 dimension

# Transpose
b = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3)
b.T                                      # shape (3, 2) — rows become columns

# Adding dimensions — essential for making shapes broadcast-compatible
v = np.array([1, 2, 3])    # shape (3,)
v[np.newaxis, :]            # shape (1, 3) — add dimension at front
v[:, np.newaxis]            # shape (3, 1) — add dimension at back
np.expand_dims(v, axis=0)  # same as v[np.newaxis, :]

# Removing dimensions of size 1
b = np.array([[[1, 2, 3]]])   # shape (1, 1, 3)
np.squeeze(b)                  # shape (3,)

# Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.stack([a, b], axis=0)       # [[1,2,3],[4,5,6]] — new axis → (2, 3)
np.concatenate([a, b])         # [1,2,3,4,5,6] — join along existing axis
```

---

## 2.7 — Linear Algebra Operations

```python
A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[5.0, 6.0], [7.0, 8.0]])

A @ B                      # matrix multiply → [[19,22],[43,50]]
A * B                      # element-wise multiply → [[5,12],[21,32]]
A.T                        # transpose → [[1,3],[2,4]]

v = np.array([1.0, 2.0, 3.0])
w = np.array([4.0, 5.0, 6.0])
np.dot(v, w)               # dot product → 32

np.linalg.inv(A)           # matrix inverse
np.linalg.solve(A, b)      # solve Ax=b (more stable than inv)
np.linalg.eig(A)           # eigenvalues and eigenvectors
np.linalg.svd(A)           # SVD decomposition

np.linalg.norm(v)          # L2 norm
np.linalg.norm(v, ord=1)   # L1 norm
np.linalg.norm(A, ord='fro') # Frobenius norm
```

### np.einsum — a preview

Expresses any sum over indices in compact notation. You do not need to master it now — just know it exists.

```python
np.einsum("ij,jk->ik", A, B)   # same as A @ B
np.einsum("i,i->", v, w)        # dot product → scalar
np.einsum("ij->ji", A)           # transpose

# Batch matrix multiply — used in transformer attention
Q = np.random.randn(8, 10, 64)   # (batch, seq, d_k)
K = np.random.randn(8, 10, 64)
scores = np.einsum("bqd,bkd->bqk", Q, K)  # (8, 10, 10)
```

---

## 2.8 — Common Pitfalls

```python
# 1. Float comparison
0.1 + 0.2 == 0.3               # False — floating point imprecision
np.isclose(0.1 + 0.2, 0.3)    # True — use this
np.allclose(arr1, arr2)        # for comparing arrays

# 2. Shape (3,) vs (3,1) vs (1,3) — these behave very differently
a = np.array([1, 2, 3])         # 1D
b = a.reshape(1, 3)              # 2D row vector
c = a.reshape(3, 1)              # 2D column vector
# b @ c → (1,1) — dot product
# c @ b → (3,3) — outer product
# Always know if your array is 1D or 2D

# 3. In-place vs creating new array
a = np.array([1.0, 2.0, 3.0])
b = a
a += 1      # modifies a IN PLACE — b also changes (same object)
a = a + 1   # creates a NEW array — b still points to old one
```

---

## 2.9 — Resources for NumPy

- NumPy official quickstart: numpy.org/doc/stable/user/quickstart.html
- CS231n Python/NumPy tutorial: cs231n.github.io/python-numpy-tutorial
- 100 NumPy Exercises (github.com/rougier/numpy-100) — do all 100

---
