# Phase 0 — NumPy Concepts

Concepts, not drills — drills are in `numpy_exercises.md` in this folder.
Sections 1.7 onward connect to `math_concepts.md` — read the relevant part
of that file alongside Sections 5 and 8 of the exercises.

---

## The Right Mindset

NumPy is not a collection of math functions. It is a different way of thinking about data. The shift: instead of "I have a list and I will loop over it," think "I have an array and I will operate on the whole thing at once."

This matters for two reasons. NumPy operations run in compiled C — they are 10–1000x faster than Python loops. And PyTorch tensors work exactly the same way. Everything you learn here transfers directly.

---

## 1.1 — What is an ndarray?

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
np.random.uniform(-1.0, 1.0, size=(3, 4)) # 3x4 uniform [-1, 1)
np.random.choice(10, size=5, replace=False)  # 5 unique picks from range(10)
np.random.permutation(5)                  # int in -> shuffled [0,1,2,3,4]

np.array([1, 2, 3], dtype=np.float32)    # 32-bit float (GPU prefers this)
np.array([1, 2, 3], dtype=np.float64)    # 64-bit float (NumPy default)
```

Why dtype matters: PyTorch uses `float32`. NumPy defaults to `float64`. You will be converting between them, so always know what you have.

### `np.random.permutation` on an array, not just an int

Give it an integer and it shuffles `arange(n)`. Give it an array instead, and it shuffles that array along **axis 0 only** — always rows for a 2D array, never columns — and returns a shuffled copy, leaving the original untouched.

```python
data = np.arange(20).reshape(5, 4)   # 5 samples, 4 features each
shuffled = np.random.permutation(data)
# rows get reordered as whole units — each row's 4 values stay together,
# exactly as they were, just in a different position. Columns are never
# touched independently.
```

This is exactly the behavior you want for a dataset: reorder which sample comes first, without scrambling which feature values belong to which sample. `np.random.permutation(data)[:10]` — shuffle then slice — is a standard pattern for sampling N rows without replacement.

### dtype upcasting

Mixing dtypes in one operation always promotes to the more precise/general type — never silently loses precision.

```python
a = np.array([1, 2, 3])                      # int64
b = np.array([1.0, 2.0, 3.0])                # float64
c = np.array([1, 2, 3], dtype=np.float32)    # float32

(a + b).dtype    # float64 — int64 + float64 -> float64
(a + c).dtype    # float64 — int64 + float32 -> float64 (needs float64 to hold int64's range)
```

---

## 1.2 — Indexing and Slicing

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

# Slices with a step: [start:end:step]
b = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12],
              [13, 14, 15, 16]])
b[::2, ::2]        # [[1,3],[9,11]] — every other row, every other column
b[::-1]            # rows reversed
b[0:3:2, 1:4:2]    # [[2,4],[10,12]] — rows 0,2 and cols 1,3

# Boolean indexing
mask = a > 5
a[mask]          # [6, 7, 8, 9] — values where mask is True
a[a > 5] = 0     # set those values to 0 in place
```

### Fancy indexing

Index with a list/array of integers to select arbitrary positions — not a contiguous range like a slice.

```python
a = np.array([10, 20, 30, 40, 50])
a[[0, 2, 3]]                # [10, 30, 40] — arbitrary rows/positions, any order, repeats allowed

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
M[[0, 2]]                   # rows 0 and 2
M[[0, 1, 2], [0, 1, 2]]     # paired indices -> diagonal: [1, 5, 9]
```

Used constantly for batching/sampling: `data[batch_indices]` pulls an arbitrary batch of rows in one call.

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

# Boolean and fancy indexing ALWAYS return a COPY, never a view
d = a[a > 1]     # boolean index -> copy
d[0] = -1
print(a)         # unchanged

e = a[[0, 1]]    # fancy index -> copy
e[0] = -1
print(a)         # unchanged
```

**The rule:** slicing → view. Boolean or fancy (integer-array) indexing → copy. Views exist for performance but cause confusing bugs — when in doubt, call `.copy()`.

---

## 1.3 — Broadcasting — The Most Important NumPy Concept

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

## 1.4 — Vectorization: Think in Arrays

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

### Vectorized conditionals: `np.where`

`np.where(condition, if_true, if_false)` — an element-wise ternary, no loop.

```python
a = np.array([1, -2, 3, -4, 5])
np.where(a > 0, a, 0)     # [1, 0, 3, 0, 5] — keep positives, zero out the rest
```

---

## 1.5 — Aggregation and Reduction

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

### `np.all` / `np.any` — checking a condition across an axis

`np.all(condition, axis=...)` is True only if *every* element along that axis satisfies the condition. `np.any` is True if *at least one* does. Both are reductions like `sum`/`mean` — same `axis` rules apply, and combine with `.sum()` to count how many rows/columns satisfy the condition.

```python
X = np.array([[1, 2, -3],
              [4, 5, 6]])

np.all(X > 0)              # False — at least one element isn't > 0
np.all(X > 0, axis=1)      # [False, True] — row 0 has a negative, row 1 doesn't
np.any(X < 0, axis=1)      # [True, False]

np.all(X > 0, axis=1).sum()   # 1 — count of rows where every value is positive
```

### Sorting: `argsort`

`np.argsort` returns the *indices* that would sort an array — not the sorted values themselves. Combine it with fancy indexing to actually reorder something (an array itself, or a second array by the first's order — e.g. reordering eigenvectors by their eigenvalues).

```python
a = np.array([30, 10, 20])
np.argsort(a)            # [1, 2, 0] — index of smallest, then next, then next
a[np.argsort(a)]          # [10, 20, 30] — a, sorted ascending
a[np.argsort(a)[::-1]]    # [30, 20, 10] — sorted descending
```

### `keepdims` — for feeding the result back into broadcasting

Reducing along an axis drops that dimension by default. `keepdims=True` keeps it as size 1, so the result still broadcasts cleanly against the original array.

```python
X = np.random.randn(4, 3)

row_sum = X.sum(axis=1)                    # shape (4,) — dimension dropped
X / row_sum                                 # ERROR — (4,3) vs (4,) don't align

row_sum_k = X.sum(axis=1, keepdims=True)   # shape (4, 1) — dimension kept
X / row_sum_k                               # works — (4,3) / (4,1) broadcasts
```

Use `keepdims=True` any time a reduction feeds back into a divide/subtract against the original array — softmax (subtract per-row max, divide by per-row sum) is the canonical example.

ML use case — normalizing features:

```python
X = np.random.randn(100, 5)    # 100 samples, 5 features
mean = X.mean(axis=0)          # shape (5,) — mean per feature
std = X.std(axis=0)            # shape (5,)
X_norm = (X - mean) / std      # (100,5) - (5,) — broadcasting handles it
# Every feature now has mean≈0, std≈1
```

---

## 1.6 — Shape Manipulation

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

# Flatten to 1D
M = np.random.randn(3, 4)
M.flatten()      # always a COPY
M.ravel()        # a VIEW when possible, falls back to a copy if it can't be

# Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.stack([a, b], axis=0)       # [[1,2,3],[4,5,6]] — new axis → (2, 3)
np.concatenate([a, b])         # [1,2,3,4,5,6] — join along existing axis

# vstack/hstack — shortcuts for the common 2D cases
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.vstack([A, B])              # shape (4, 2) — stacked as more rows
np.hstack([A, B])              # shape (2, 4) — stacked as more columns

# column_stack — turn separate 1D vectors into columns of a 2D array
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
np.column_stack([x1, x2])      # [[1,4],[2,5],[3,6]] — shape (3, 2)
```

---

## 1.7 — Linear Algebra Operations

```python
A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[5.0, 6.0], [7.0, 8.0]])

A @ B                      # matrix multiply → [[19,22],[43,50]]
A * B                      # element-wise multiply → [[5,12],[21,32]]
A.T                        # transpose → [[1,3],[2,4]]

v = np.array([1.0, 2.0, 3.0])
w = np.array([4.0, 5.0, 6.0])
np.dot(v, w)               # dot product → 32

b_vec = np.array([5.0, 6.0])
np.linalg.inv(A)              # matrix inverse
np.linalg.solve(A, b_vec)     # solve Ax=b — more stable than inv(A) @ b
np.linalg.eig(A)              # eigenvalues and eigenvectors
np.linalg.svd(A)              # SVD decomposition

np.linalg.norm(v)          # L2 norm
np.linalg.norm(v, ord=1)   # L1 norm
np.linalg.norm(A, ord='fro') # Frobenius norm

# np.diag does two different things depending on the input's ndim:
np.diag(A)                    # A is 2D -> extracts the diagonal, shape (2,)
np.diag(np.array([1.0, 2.0])) # input is 1D -> builds a diagonal matrix, shape (2, 2)
```

Deeper treatment of what eigenvalues/SVD *mean* and PCA built from them: `math_concepts.md` 1.1.

---

## 1.8 — einsum

Einstein summation notation — one compact syntax for sums, products, transposes, matrix multiplies, and batched versions of all of them.

### The one rule

`np.einsum("input_labels->output_labels", *arrays)`. Every axis gets a letter.

- A letter that appears in the **inputs but not the output** gets summed over.
- A letter that appears in **both inputs and output** is kept, matched position-by-position across arrays.
- Repeating a letter across two inputs means "multiply element-wise along that axis, aligned by the letter" — combined with the summation rule above, that's how it produces dot products and matrix multiplies.

Build it up from the simplest cases:

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
A = np.random.randn(3, 4)
B = np.random.randn(4, 5)

np.einsum("i->", a)          # sum all elements — same as a.sum()
np.einsum("ij->ji", A)       # transpose — same as A.T
np.einsum("ij->i", A)        # row sums — same as A.sum(axis=1)
np.einsum("ij->j", A)        # column sums — same as A.sum(axis=0)

np.einsum("i,i->", a, b)     # dot product — "i" in both inputs, absent from
                              # output -> multiply elementwise then sum -> scalar
                              # same as np.dot(a, b)

np.einsum("i,j->ij", a, b)   # outer product — "i" and "j" each only appear
                              # once, both kept -> every pairwise product
                              # same as np.outer(a, b), shape (3, 3)

np.einsum("ij,jk->ik", A, B) # matrix multiply — "j" appears in both inputs,
                              # absent from output -> summed over
                              # same as A @ B

M = np.random.randn(4, 4)
np.einsum("ii->i", M)        # diagonal — same as np.diag(M)
np.einsum("ij,ij->i", A, A)  # sum of squares per row — same as (A*A).sum(axis=1),
                              # also same as np.diag(A @ A.T) but without
                              # ever forming the full (3,3) gram matrix
```

### Batched versions

Add a batch letter (conventionally `b`) that appears unchanged in every input and the output — it's never summed, just carried along.

```python
# Batch matmul: 8 independent (3,4) @ (4,5) multiplies at once
batch_A = np.random.randn(8, 3, 4)
batch_B = np.random.randn(8, 4, 5)
np.einsum("bij,bjk->bik", batch_A, batch_B)   # shape (8, 3, 5)
# same as np.stack([batch_A[i] @ batch_B[i] for i in range(8)]) — einsum
# does it in one vectorized call, no Python loop

# Attention scores: Q @ K.T per batch, without ever forming K.T explicitly
Q = np.random.randn(2, 5, 8)   # (batch, seq, d_k)
K = np.random.randn(2, 5, 8)
scores = np.einsum("bqd,bkd->bqk", Q, K)   # shape (2, 5, 5)
# "b" carried through unchanged, "d" appears in both inputs and not the
# output -> summed over (that's the dot product between each query and key)
```

This last pattern is exactly the raw attention-score computation inside a transformer's self-attention.

---

## 1.9 — Numerical Stability

Two operations blow up quietly: `exp` of a large number overflows to `inf`, and `log` of exactly `0` returns `-inf`. Both happen routinely in ML code (softmax, cross-entropy) and both have standard fixes.

```python
# exp overflow
x = np.array([1000.0, 1001.0, 1002.0])
np.exp(x)          # [inf, inf, inf]

# log(0)
np.log(0.0)         # -inf
```

**Fix for `log`:** add a small epsilon so it never sees exactly zero.

```python
eps = 1e-9
probs = np.array([0.5, 0.3, 0.2, 0.0])
np.log(probs + eps)   # finite everywhere, last value just very negative
```

**Fix for division by zero:** don't compute `x / y` directly if `y` might be 0 — swap in a safe value first with `np.where`.

```python
counts = np.array([10, 5, 0, 3])
values = np.array([1.0, 2.0, 3.0, 4.0])
values / counts                                          # inf at index 2
np.where(counts == 0, 0.0, values / np.where(counts == 0, 1, counts))
# [0.1, 0.4, 0.0, 1.33] — the inner np.where avoids the division ever
# happening on a 0; the outer one picks the final safe value
```

**Fix for `exp` overflow — the subtract-max trick.** `log(sum(exp(x)))` ("log-sum-exp") is the core of softmax and cross-entropy. Subtracting the max before exponentiating gives the identical mathematical result but never overflows, because the largest exponent is now exactly 0:

```python
def log_sum_exp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))

x = np.array([1000.0, 1001.0, 1002.0])
np.log(np.sum(np.exp(x)))   # inf — naive version overflows
log_sum_exp(x)                # 1002.41 — stable version doesn't
```

This is exactly why `math_concepts.md`'s `softmax` implementation subtracts `np.max(logits, ..., keepdims=True)` before calling `np.exp`.

---

## 1.10 — Common Pitfalls

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

# 4. Integer dtypes overflow silently on element-wise ops (not on .sum() —
#    NumPy widens the accumulator there). Constructing an out-of-range
#    literal now raises immediately instead of wrapping:
np.array([200], dtype=np.int8)      # raises OverflowError (int8 max is 127)
a = np.array([100], dtype=np.int8)
a + a                                 # [-56] — 200 wraps silently, still int8
```

---

## 1.11 — Resources for NumPy

- NumPy official quickstart: numpy.org/doc/stable/user/quickstart.html
- CS231n Python/NumPy tutorial: cs231n.github.io/python-numpy-tutorial
- 100 NumPy Exercises (github.com/rougier/numpy-100) — do all 100

---

*Last updated: 2026-08-15*
