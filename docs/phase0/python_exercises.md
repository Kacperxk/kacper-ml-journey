# Python Exercises — Phase 0 Proficiency
## 2–3 days of focused practice | ~70 exercises + Git/GitHub drills

---

> **How to use this document:** Work through sections in order. Each section builds on the previous. These are not beginner exercises — they target the specific Python patterns that appear constantly in ML engineering code. Do every exercise in a proper `.py` file, not a notebook. Run it. Break it. Fix it.

> **The rule:** for every exercise involving a prediction, write the expected output as a comment before running. If you are wrong, understand why before moving on. Being wrong and understanding why is more valuable than being right.

> **Git rule:** every exercise section gets its own commit. By the end of this document your repo will have a clean, meaningful history. That is part of the exercise.

---

> **Note:** the three projects originally at the end of this file (Config
> Manager, Data Pipeline, Mini ML Framework) have been removed — they're
> superseded by `docs/PHASE0_PROJECTS.md`'s single canonical project list.
> Data Pipeline became Core Project 2; Config Manager and Mini ML Framework
> became stretch projects. Full specs are preserved there.

---

# SECTION 1 — Identity, Mutability, and Memory

*These feel basic but they cause real bugs in ML code. Make sure they are completely solid.*

---

**Exercise 1.1** — Variables are labels. Predict every print output before running.

```python
# Block A
a = [1, 2, 3]
b = a
b.append(4)
print(a)      # ?
print(b)      # ?
print(a is b) # ?

# Block B
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)      # ?
print(b)      # ?
print(a is b) # ?

# Block C
x = 5
y = x
y += 1
print(x)      # ?
print(y)      # ?
print(x is y) # ?

# Block D
s1 = "hello"
s2 = s1
s2 = s2 + " world"
print(s1)     # ?
print(s2)     # ?
```

After running, write a one-paragraph comment explaining the difference between mutation and rebinding.

---

**Exercise 1.2** — Mutable default argument. This is one of Python's most famous traps.

```python
# Version 1 — buggy
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))   # ?
print(append_to(2))   # ?  — surprise
print(append_to(3))   # ?  — even more surprising

# Version 2 — correct
def append_to_fixed(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

print(append_to_fixed(1))   # ?
print(append_to_fixed(2))   # ?
```

Then: write a function `make_config` that takes keyword arguments for `lr`, `epochs`, and `hidden_sizes` (a list). The default for `hidden_sizes` should be `[128, 64]`. Make sure calling it twice with no arguments gives two independent lists that can be modified without affecting each other. Verify this with an assertion.

---

**Exercise 1.3** — Copying: shallow vs deep.

```python
import copy

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy
shallow = original.copy()
shallow[0][0] = 999
print(original[0][0])   # ?  — changed or not?

# Deep copy
original2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep = copy.deepcopy(original2)
deep[0][0] = 999
print(original2[0][0])  # ?  — changed or not?
```

Write the rule as a comment: "Shallow copy creates a new container but... Deep copy creates..."

Then: write a function `safe_clone(data: list) -> list` that always returns a fully independent copy regardless of nesting depth. Test it on a list of lists of lists.

---

**Exercise 1.4** — `is` vs `==`. These are completely different things.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # ?
print(a is b)    # ?
print(a is c)    # ?

# Small integer caching — Python caches small ints
x = 256
y = 256
print(x is y)   # ?  (True — cached)

x = 257
y = 257
print(x is y)   # ?  (might be False — implementation detail)

# String interning
s1 = "hello"
s2 = "hello"
print(s1 is s2)   # ?  (True — Python interns short strings)

s3 = "hello world"
s4 = "hello world"
print(s3 is s4)   # ?  (might be False)
```

The rule: use `==` to compare values, `is` to check identity (same object in memory). The only correct use of `is` in normal code: `x is None` and `x is not None`.

---

# SECTION 2 — Comprehensions and Functional Patterns

*These are the difference between code that reads like a Python engineer wrote it and code that reads like a C programmer wrote it.*

---

**Exercise 2.1** — List comprehensions: from loops to one-liners.

Rewrite each loop as a list comprehension. The result must be identical.

```python
# Loop 1
result = []
for x in range(10):
    result.append(x ** 2)

# Loop 2
result = []
for x in range(20):
    if x % 2 == 0:
        result.append(x)

# Loop 3
words = ["hello", "world", "python", "ml"]
result = []
for word in words:
    result.append(word.upper())

# Loop 4 — nested
result = []
for i in range(3):
    for j in range(3):
        result.append((i, j))

# Loop 5 — nested with condition
result = []
for i in range(5):
    for j in range(5):
        if i != j:
            result.append(i * j)
```

For each, verify the comprehension gives identical output to the loop using `==`.

---

**Exercise 2.2** — Dict and set comprehensions.

```python
# Given this data:
students = [
    ("Michal", 4.5),
    ("Anna", 5.0),
    ("Piotr", 3.8),
    ("Kasia", 4.2),
]

# Task A: create a dict mapping name → grade using a dict comprehension
grades = ...    # {"Michal": 4.5, "Anna": 5.0, ...}

# Task B: create a dict of name → grade only for students with grade >= 4.0
good_students = ...

# Task C: create a set of all unique first letters of student names
first_letters = ...    # {'M', 'A', 'P', 'K'}

# Task D: given a list of words with duplicates, count frequency of each word
words = ["the", "quick", "the", "brown", "fox", "the", "quick"]
freq = ...     # {"the": 3, "quick": 2, "brown": 1, "fox": 1}
# Use a dict comprehension with words.count() — then think of a better way

# Task E: invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = ...    # {1: "a", 2: "b", 3: "c"}
```

---

**Exercise 2.3** — Generator expressions: when to use them instead of list comprehensions.

```python
import sys

# Compare memory usage
n = 1_000_000

list_comp = [x**2 for x in range(n)]
gen_expr  = (x**2 for x in range(n))

print(sys.getsizeof(list_comp))   # large — stores all values
print(sys.getsizeof(gen_expr))    # tiny — stores only the generator state

# Generators are lazy — they compute values on demand
gen = (x**2 for x in range(5))
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4
# Call next() two more times, then call it once more — what happens?
```

Write these using generator expressions (not list comprehensions):
```python
# A: sum of squares from 0 to 999
total = sum(...)

# B: first 10 even squares (squares that are divisible by 2)
# Use a generator expression inside list()
even_squares = list(...)

# C: True if any number in range(1000) is divisible by 997
any_divisible = any(...)
```

---

**Exercise 2.4** — `map`, `filter`, `zip`, `enumerate` — know when each is idiomatic.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["alpha", "beta", "gamma", "delta"]

# For each, write the result first as a list comprehension,
# then as the equivalent using map/filter/zip.

# A: square each number
squares_comp = [x**2 for x in numbers]
squares_map  = list(map(..., numbers))

# B: keep only odd numbers
odds_comp   = [x for x in numbers if x % 2 != 0]
odds_filter = list(filter(..., numbers))

# C: pair each word with its length
pairs_comp = [(w, len(w)) for w in words]
pairs_zip  = list(zip(words, map(len, words)))

# D: pair each word with its index
indexed_comp = [(i, w) for i, w in enumerate(words)]
indexed_enum = list(enumerate(words))

# E: combine two lists into a dict
keys   = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
d = dict(zip(keys, values))
# Then: what happens if keys and values have different lengths?
# Predict, then test with a shorter values list.
```

For each pair, note which version is more readable. There is no single right answer — the point is to have both available.

---

**Exercise 2.5** — Comprehensions in ML contexts. These exact patterns appear in training loops and data pipelines.

```python
# Dataset represented as a list of (feature_vector, label) tuples
import random
random.seed(42)

dataset = [
    ([random.gauss(0, 1) for _ in range(4)], random.randint(0, 2))
    for _ in range(100)
]

# Task A: extract all labels into a flat list
labels = [...]

# Task B: extract all feature vectors
features = [...]

# Task C: count how many samples belong to each class
# Result: {0: count0, 1: count1, 2: count2}
class_counts = {cls: sum(1 for _, label in dataset if label == cls)
                for cls in range(3)}

# Task D: filter to only class 0 and class 1 (binary problem)
binary_dataset = [(feat, label) for feat, label in dataset if label != 2]

# Task E: create a mini-batch by taking every 10th sample
mini_batch = dataset[::10]   # what is the length?

# Task F: flatten a list of batches back into samples
batches = [dataset[i:i+10] for i in range(0, 100, 10)]
flat = [sample for batch in batches for sample in batch]
assert flat == dataset   # should pass
```

---

# SECTION 3 — Functions in Depth

---

**Exercise 3.1** — `*args` and `**kwargs`: understand them mechanically.

```python
def inspect(*args, **kwargs):
    print(f"args type:   {type(args)}")    # always a tuple
    print(f"kwargs type: {type(kwargs)}")  # always a dict
    print(f"args:   {args}")
    print(f"kwargs: {kwargs}")

# Predict the output for each call:
inspect(1, 2, 3)
inspect(a=1, b=2)
inspect(1, 2, x=3, y=4)
inspect()
```

Now write these functions:

```python
def mean(*numbers: float) -> float:
    """Return the mean of any number of floats."""
    pass

def create_model_config(model_type: str, **hyperparams) -> dict:
    """
    Return a config dict with model_type and all hyperparams.
    Example: create_model_config("mlp", lr=0.001, hidden=128)
    → {"model_type": "mlp", "lr": 0.001, "hidden": 128}
    """
    pass

def run_experiment(dataset: str, *metrics: str, verbose: bool = False, **model_kwargs):
    """
    Mixed signature: positional, *args, keyword-only, **kwargs.
    Print a summary of the experiment configuration.
    """
    pass

# Test:
print(mean(1, 2, 3, 4, 5))      # 3.0
print(mean(10.0, 20.0))          # 15.0
cfg = create_model_config("transformer", layers=6, heads=8, lr=0.0001)
assert cfg["model_type"] == "transformer"
assert cfg["layers"] == 6
```

---

**Exercise 3.2** — Unpacking operators: `*` and `**` in call position.

```python
# Unpacking into function calls
def add(a, b, c):
    return a + b + c

args = (1, 2, 3)
kwargs = {"a": 1, "b": 2, "c": 3}

print(add(*args))     # same as add(1, 2, 3)
print(add(**kwargs))  # same as add(a=1, b=2, c=3)

# Unpacking into list/dict literals
first = [1, 2, 3]
second = [4, 5, 6]
combined = [*first, *second]       # [1, 2, 3, 4, 5, 6]
print(combined)

config_base = {"lr": 0.001, "epochs": 10}
config_override = {"epochs": 20, "batch_size": 32}
merged = {**config_base, **config_override}
print(merged)   # {"lr": 0.001, "epochs": 20, "batch_size": 32}
# Note: later keys win on conflict
```

Tasks:
```python
# A: write a function that merges any number of dicts, later dicts win
def merge_configs(*dicts: dict) -> dict:
    pass

# B: given a function signature, call it correctly
def train(model, optimizer, loss_fn, *, epochs=10, device="cpu"):
    pass

# These should all work:
base = {"epochs": 5, "device": "cuda"}
train(None, None, None, **base)
train(None, None, None, epochs=20)
# This should FAIL with a TypeError — why?
# train(None, None, None, 10, "cuda")   — uncomment and understand the error
```

---

**Exercise 3.3** — Closures: capture, mutation, and the cell.

```python
# Exercise A: basic capture
def outer(x):
    def inner(y):
        return x + y    # x is captured from outer's scope
    return inner

add_10 = outer(10)
add_20 = outer(20)
print(add_10(5))   # ?
print(add_20(5))   # ?
print(add_10(add_20(0)))  # ?

# Exercise B: the late-binding gotcha — famous Python trap
functions = []
for i in range(5):
    functions.append(lambda: i)   # all lambdas capture the same 'i'

print([f() for f in functions])   # ? — might surprise you
```

Fix the lambda trap using a default argument:
```python
functions_fixed = []
for i in range(5):
    functions_fixed.append(lambda i=i: i)   # i=i creates a new binding each time

print([f() for f in functions_fixed])   # [0, 1, 2, 3, 4]
```

Now write these closures:
```python
def make_multiplier(factor: float):
    """Return a function that multiplies its input by factor."""
    pass

def make_counter(start: int = 0, step: int = 1):
    """
    Return a counter function. Each call returns the next value.
    Uses nonlocal to mutate the captured variable.
    """
    count = start
    def counter():
        nonlocal count
        # increment count by step and return current value
        pass
    return counter

def make_running_average():
    """
    Return a function that accepts one number at a time
    and returns the running average of all numbers seen so far.
    """
    pass

# Tests:
triple = make_multiplier(3)
assert triple(5) == 15
assert triple(10) == 30

c = make_counter(start=0, step=2)
assert c() == 0
assert c() == 2
assert c() == 4

avg = make_running_average()
assert avg(10) == 10.0
assert avg(20) == 15.0
assert avg(30) == 20.0
```

---

**Exercise 3.4** — Decorators: build them from scratch.

Start from first principles — no shortcuts.

```python
# Part A: write a decorator that prints "calling <function_name>" before
# calling the function and "done" after. Use functools.wraps.
import functools

def trace(func):
    pass

@trace
def add(a, b):
    return a + b

add(3, 4)
# Should print:
# calling add
# done

# Part B: a decorator with an argument (a decorator factory)
def repeat(n: int):
    """Calls the decorated function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("hello")

say_hello()   # prints "hello" three times

# Part C: a caching decorator (memoization)
def memoize(func):
    """Cache results. Same arguments → return cached result."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Without memoize: fibonacci(35) takes several seconds
# With memoize: fibonacci(35) is instant
print(fibonacci(35))

# Part D: a type-checking decorator
def typecheck(func):
    """
    Verify that all arguments match the function's type hints at call time.
    Raise TypeError with a clear message if they don't.
    Use func.__annotations__ to get the hints.
    """
    import inspect
    sig = inspect.signature(func)
    hints = func.__annotations__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        for param_name, value in bound.arguments.items():
            if param_name in hints and param_name != "return":
                expected_type = hints[param_name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"{func.__name__}() argument '{param_name}' "
                        f"must be {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
        return func(*args, **kwargs)
    return wrapper

@typecheck
def power(base: float, exponent: int) -> float:
    return base ** exponent

print(power(2.0, 3))      # 8.0 — works
# power(2.0, 3.5)         # should raise TypeError — test it
# power("two", 3)         # should raise TypeError — test it
```

---

**Exercise 3.5** — Generators: yield, send, and the iterator protocol.

```python
# Part A: basic generators
def countdown(n: int):
    """Yield n, n-1, n-2, ..., 1, 0"""
    pass

def fibonacci_gen():
    """Infinite generator of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take the first 10 Fibonacci numbers:
from itertools import islice
first_10 = list(islice(fibonacci_gen(), 10))
print(first_10)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Part B: generator as a data pipeline
def read_numbers(path: str):
    """Yield one integer per line from a file, skipping blank lines."""
    pass

def filter_even(numbers):
    """Yield only even numbers from an iterable."""
    pass

def square_each(numbers):
    """Yield x**2 for each x in numbers."""
    pass

# These chain together with no intermediate lists:
# pipeline = square_each(filter_even(read_numbers("data.txt")))

# Part C: batch generator — the exact pattern used in ML training
def batch_generator(data: list, batch_size: int, shuffle: bool = False, seed: int = 42):
    """
    Yield batches of data.
    If shuffle=True, shuffle the data before batching.
    The last batch may be smaller than batch_size.
    """
    import random
    if shuffle:
        data = data.copy()
        random.seed(seed)
        random.shuffle(data)
    for start in range(0, len(data), batch_size):
        yield data[start : start + batch_size]

# Test:
data = list(range(10))
batches = list(batch_generator(data, batch_size=3))
print(batches)   # [[0,1,2], [3,4,5], [6,7,8], [9]]

# Verify last batch is partial:
assert len(batches[-1]) == 1

# Verify shuffle works:
batches_shuffled = list(batch_generator(data, batch_size=3, shuffle=True))
flat = [x for batch in batches_shuffled for x in batch]
assert sorted(flat) == data   # same elements, different order
```

---

# SECTION 4 — OOP in Depth

---

**Exercise 4.1** — Dunder methods: make your classes feel like Python.

Implement a `BoundedList` class — a list that cannot grow beyond a maximum size:

```python
class BoundedList:
    """
    A list-like container with a maximum capacity.
    When full, adding items raises an OverflowError.
    """

    def __init__(self, max_size: int):
        pass

    def append(self, item) -> None:
        """Add item. Raise OverflowError if at capacity."""
        pass

    def __len__(self) -> int:
        pass

    def __getitem__(self, index: int):
        pass

    def __setitem__(self, index: int, value) -> None:
        pass

    def __delitem__(self, index: int) -> None:
        pass

    def __contains__(self, item) -> bool:
        """Supports: 'x in bounded_list'"""
        pass

    def __iter__(self):
        """Supports: 'for x in bounded_list'"""
        pass

    def __repr__(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        """Equal if same contents and same max_size."""
        pass

    @property
    def is_full(self) -> bool:
        pass

    @property
    def remaining(self) -> int:
        """How many more items can be added."""
        pass
```

Tests — all must pass:
```python
bl = BoundedList(max_size=3)
bl.append(10)
bl.append(20)
bl.append(30)
assert len(bl) == 3
assert bl.is_full
assert bl.remaining == 0
assert bl[0] == 10
assert bl[-1] == 30
assert 20 in bl
assert 99 not in bl

try:
    bl.append(40)
    assert False, "Should have raised OverflowError"
except OverflowError:
    pass

# Iteration
values = list(bl)
assert values == [10, 20, 30]

# Modification
bl[1] = 99
assert bl[1] == 99

# Deletion
del bl[0]
assert len(bl) == 2
assert bl.remaining == 1

# Equality
a = BoundedList(3)
b = BoundedList(3)
a.append(1); b.append(1)
assert a == b

print("BoundedList: all tests passed")
```

---

**Exercise 4.2** — Properties: controlled access with validation.

```python
class LearningRateScheduler:
    """
    Manages a learning rate for model training.
    Enforces constraints and tracks history.
    """

    def __init__(self, initial_lr: float, min_lr: float = 1e-6, max_lr: float = 1.0):
        # Validate that initial_lr is between min_lr and max_lr
        # Store the history of all LR values as a list
        pass

    @property
    def lr(self) -> float:
        """Current learning rate."""
        pass

    @lr.setter
    def lr(self, value: float) -> None:
        """
        Set a new learning rate.
        Raise ValueError if value < min_lr or value > max_lr.
        Append new value to history.
        """
        pass

    @property
    def history(self) -> list:
        """All learning rate values seen so far (read-only)."""
        # Return a copy so callers cannot modify the internal history
        pass

    @property
    def n_updates(self) -> int:
        """How many times the LR has been set (not counting initial)."""
        pass

    def decay(self, factor: float) -> None:
        """Multiply current LR by factor. Clamp to min_lr if needed."""
        pass

    def reset(self) -> None:
        """Reset to initial LR, clear history."""
        pass

    def __repr__(self) -> str:
        return f"LRScheduler(lr={self.lr:.6f}, updates={self.n_updates})"


# Tests:
scheduler = LearningRateScheduler(initial_lr=0.01, min_lr=1e-5, max_lr=0.1)
assert scheduler.lr == 0.01
assert scheduler.n_updates == 0

scheduler.lr = 0.001
assert scheduler.lr == 0.001
assert scheduler.n_updates == 1

try:
    scheduler.lr = 10.0   # above max_lr
    assert False, "Should raise ValueError"
except ValueError:
    pass

scheduler.decay(0.5)
assert abs(scheduler.lr - 0.0005) < 1e-10

# History returns a copy
h = scheduler.history
h.append(999.0)
assert 999.0 not in scheduler.history   # internal history unchanged

scheduler.reset()
assert scheduler.lr == 0.01
assert scheduler.n_updates == 0

print("LearningRateScheduler: all tests passed")
```

---

**Exercise 4.3** — Class methods and static methods: factory patterns.

```python
from typing import Optional
import json
import csv
import io

class Dataset:
    """
    A simple supervised learning dataset.
    Multiple ways to construct it — this is the factory pattern.
    """

    def __init__(self, features: list[list[float]], labels: list[int], name: str = "unnamed"):
        if len(features) != len(labels):
            raise ValueError(
                f"features and labels must match: {len(features)} vs {len(labels)}"
            )
        self._features = [list(f) for f in features]   # deep copy
        self._labels = list(labels)
        self.name = name
        self._n_features = len(features[0]) if features else 0

    @classmethod
    def from_dict(cls, data: dict, name: str = "unnamed") -> "Dataset":
        """
        Build from dict with keys "features" and "labels".
        Validate that the dict has the right structure.
        """
        pass

    @classmethod
    def from_csv_string(cls, csv_text: str, label_col: int = -1, name: str = "unnamed") -> "Dataset":
        """
        Parse a CSV string where all columns are numeric.
        label_col: which column is the label (-1 = last column).
        All other columns are features.
        """
        pass

    @classmethod
    def from_json_string(cls, json_text: str) -> "Dataset":
        """Parse JSON string with structure {"name": ..., "features": ..., "labels": ...}"""
        pass

    @staticmethod
    def validate_features(features: list[list[float]]) -> bool:
        """
        Return True if all feature vectors have the same length.
        Return False otherwise.
        """
        pass

    @staticmethod
    def encode_labels(labels: list) -> tuple[list[int], dict]:
        """
        Convert arbitrary labels (strings, etc.) to integers 0, 1, 2...
        Return (encoded_labels, label_to_int_mapping).
        """
        pass

    def __len__(self) -> int:
        return len(self._labels)

    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, n_samples={len(self)}, n_features={self._n_features})"

    def to_dict(self) -> dict:
        return {"name": self.name, "features": self._features, "labels": self._labels}


# Tests:
# From dict
d = Dataset.from_dict({
    "features": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    "labels": [0, 1, 0],
}, name="test")
assert len(d) == 3

# From CSV string
csv_text = "1.0,2.0,0\n3.0,4.0,1\n5.0,6.0,0\n"
d2 = Dataset.from_csv_string(csv_text, label_col=-1)
assert len(d2) == 3

# validate_features
assert Dataset.validate_features([[1, 2], [3, 4], [5, 6]]) is True
assert Dataset.validate_features([[1, 2], [3, 4, 5]]) is False

# encode_labels
encoded, mapping = Dataset.encode_labels(["cat", "dog", "cat", "fish"])
assert set(encoded) == {0, 1, 2}
assert mapping["cat"] != mapping["dog"]

print("Dataset: all tests passed")
```

---

**Exercise 4.4** — Inheritance and abstract base classes.

```python
from abc import ABC, abstractmethod
from typing import Any

class Metric(ABC):
    """
    Abstract base class for evaluation metrics.
    Subclasses must implement compute() and name.
    """

    def __init__(self):
        self._history: list[float] = []

    @property
    @abstractmethod
    def name(self) -> str:
        """The metric's name (e.g., 'accuracy', 'mse')."""
        pass

    @abstractmethod
    def compute(self, y_true: list, y_pred: list) -> float:
        """Compute the metric from true and predicted values."""
        pass

    def update(self, y_true: list, y_pred: list) -> float:
        """Compute and store the result in history."""
        value = self.compute(y_true, y_pred)
        self._history.append(value)
        return value

    @property
    def history(self) -> list[float]:
        return list(self._history)

    @property
    def best(self) -> Optional[float]:
        """Return best value from history, or None if history is empty."""
        pass

    def reset(self) -> None:
        self._history.clear()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Accuracy(Metric):
    """Fraction of correct predictions (for classification)."""

    @property
    def name(self) -> str:
        return "accuracy"

    def compute(self, y_true: list, y_pred: list) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have same length")
        return sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)

    @property
    def best(self) -> Optional[float]:
        """For accuracy, best = maximum."""
        return max(self._history) if self._history else None


class MSE(Metric):
    """Mean Squared Error (for regression)."""

    @property
    def name(self) -> str:
        return "mse"

    def compute(self, y_true: list, y_pred: list) -> float:
        return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)

    @property
    def best(self) -> Optional[float]:
        """For MSE, best = minimum."""
        return min(self._history) if self._history else None


class MAE(Metric):
    """Implement this one yourself."""
    pass


class MetricTracker:
    """
    Tracks multiple metrics across training epochs.
    """

    def __init__(self, *metrics: Metric):
        self.metrics = {m.name: m for m in metrics}

    def update(self, epoch: int, y_true: list, y_pred: list) -> dict[str, float]:
        """Update all metrics and return dict of current values."""
        return {name: m.update(y_true, y_pred) for name, m in self.metrics.items()}

    def summary(self) -> dict[str, dict[str, float]]:
        """Return dict of metric_name → {"current": ..., "best": ...}"""
        pass

    def reset_all(self) -> None:
        for m in self.metrics.values():
            m.reset()


# Tests:
# Cannot instantiate abstract class
try:
    m = Metric()
    assert False, "Should raise TypeError"
except TypeError:
    pass

acc = Accuracy()
assert acc.best is None

v1 = acc.update([0, 1, 1, 0], [0, 1, 0, 0])
v2 = acc.update([1, 1, 1, 1], [1, 1, 1, 0])
assert abs(v1 - 0.75) < 1e-10
assert abs(v2 - 0.75) < 1e-10
assert acc.best == 0.75

tracker = MetricTracker(Accuracy(), MSE())
results = tracker.update(1, [0, 1, 1], [0, 1, 0])
assert "accuracy" in results
assert "mse" in results

print("Metric system: all tests passed")
```

---

**Exercise 4.5** — Context managers: the `__enter__` / `__exit__` protocol.

```python
import time
import logging

class Timer:
    """
    Context manager that measures elapsed time.
    
    Usage:
        with Timer("forward pass") as t:
            do_computation()
        print(t.elapsed)   # seconds
    """

    def __init__(self, name: str = "", verbose: bool = True):
        self.name = name
        self.verbose = verbose
        self.elapsed: float = 0.0

    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.elapsed = time.perf_counter() - self._start
        if self.verbose:
            label = f"[{self.name}] " if self.name else ""
            print(f"{label}elapsed: {self.elapsed:.4f}s")
        return False   # do not suppress exceptions


class SuppressErrors:
    """
    Context manager that suppresses specified exception types.
    
    Usage:
        with SuppressErrors(ValueError, KeyError):
            risky_operation()   # if ValueError or KeyError, just continues
    """

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self) -> "SuppressErrors":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # Return True to suppress, False to re-raise
        if exc_type is not None:
            return issubclass(exc_type, self.exception_types)
        return False


class TempDirectory:
    """
    Context manager that creates a temporary directory on enter
    and deletes it (with all contents) on exit.
    """
    import os
    import shutil
    import tempfile

    def __init__(self, prefix: str = "tmp_"):
        self.prefix = prefix
        self.path: Optional[str] = None

    def __enter__(self) -> str:
        import tempfile
        self.path = tempfile.mkdtemp(prefix=self.prefix)
        return self.path   # give the caller the path

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        import shutil
        if self.path:
            shutil.rmtree(self.path)
        return False


# Tests:
with Timer("test", verbose=True) as t:
    time.sleep(0.05)
assert t.elapsed >= 0.04   # should be ~0.05s

with SuppressErrors(ValueError):
    int("not_a_number")   # normally raises ValueError — should be suppressed
print("After suppressed error — code continues")

with SuppressErrors(TypeError):
    int("not_a_number")   # ValueError — NOT in suppressed list, should propagate? Test it.

import os
with TempDirectory(prefix="test_") as tmpdir:
    test_file = os.path.join(tmpdir, "hello.txt")
    with open(test_file, "w") as f:
        f.write("hello")
    assert os.path.exists(test_file)

assert not os.path.exists(tmpdir)   # cleaned up
print("Context managers: all tests passed")
```

---

# SECTION 5 — Error Handling and Logging

---

**Exercise 5.1** — Custom exception hierarchy.

Design a proper exception hierarchy for a data loading system:

```python
class DataError(Exception):
    """Base class for all data-related errors."""
    pass

class FileFormatError(DataError):
    """Raised when a file has an unexpected format."""
    def __init__(self, path: str, expected: str, got: str):
        self.path = path
        self.expected = expected
        self.got = got
        super().__init__(f"File {path!r}: expected {expected}, got {got}")

class ColumnMissingError(DataError):
    """Raised when a required column is absent from the dataset."""
    def __init__(self, column: str, available: list[str]):
        self.column = column
        self.available = available
        super().__init__(
            f"Column {column!r} not found. Available: {available}"
        )

class ShapeMismatchError(DataError):
    """Raised when array shapes are incompatible."""
    def __init__(self, expected: tuple, got: tuple, context: str = ""):
        self.expected = expected
        self.got = got
        msg = f"Shape mismatch: expected {expected}, got {got}"
        if context:
            msg = f"{context}: {msg}"
        super().__init__(msg)

class ValidationError(DataError):
    """Raised when data fails validation checks."""
    pass
```

Now write a function that uses them properly:
```python
def load_and_validate(path: str, required_columns: list[str], expected_shape: tuple):
    """
    Load a CSV-like data structure and validate it.
    Raise appropriate custom exceptions for each failure mode.
    """
    pass

# Test by calling with bad inputs and catching specific exceptions:
try:
    load_and_validate("nonexistent.csv", ["a", "b"], (100, 2))
except FileNotFoundError:
    print("Caught FileNotFoundError")

try:
    load_and_validate("data.csv", ["missing_col"], (100, 2))
except ColumnMissingError as e:
    print(f"Missing column: {e.column}")
except DataError as e:
    print(f"General data error: {e}")
```

---

**Exercise 5.2** — Proper error handling patterns.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)

# Pattern 1: Log and re-raise
def load_checkpoint(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        logger.error("Checkpoint not found: %s", path)
        raise   # re-raise — let the caller decide what to do
    except json.JSONDecodeError as e:
        logger.error("Corrupt checkpoint %s: %s", path, e)
        raise ValueError(f"Checkpoint {path!r} is corrupted") from e

# Pattern 2: Log and return a sensible default
def load_config(path: str) -> dict:
    defaults = {"lr": 0.001, "epochs": 10}
    try:
        with open(path) as f:
            import json
            config = json.load(f)
            logger.info("Loaded config from %s", path)
            return config
    except FileNotFoundError:
        logger.warning("Config not found at %s, using defaults", path)
        return defaults

# Pattern 3: Collect errors and report all at once
def validate_config(config: dict) -> list[str]:
    """Return a list of all validation errors (not just the first one)."""
    errors = []
    if "lr" not in config:
        errors.append("Missing required key: 'lr'")
    elif not isinstance(config["lr"], (int, float)):
        errors.append(f"'lr' must be a number, got {type(config['lr']).__name__}")
    elif config["lr"] <= 0:
        errors.append(f"'lr' must be positive, got {config['lr']}")

    if "epochs" not in config:
        errors.append("Missing required key: 'epochs'")
    elif not isinstance(config["epochs"], int):
        errors.append(f"'epochs' must be int, got {type(config['epochs']).__name__}")
    elif config["epochs"] < 1:
        errors.append(f"'epochs' must be >= 1, got {config['epochs']}")

    return errors

# Test:
errors = validate_config({"lr": -0.001, "epochs": 0})
assert len(errors) == 2   # two errors collected
for e in errors:
    print(f"  Error: {e}")
```

---

# SECTION 6 — Type Hints in Practice

*Type hints are documentation that tools can verify. Learn to write them correctly.*

---

**Exercise 6.1** — Type hint the following functions correctly. Use `from typing import` whatever you need.

```python
from typing import Optional, Union, List, Dict, Tuple, Callable, Iterator, TypeVar

# A: simple types
def greet(name: str, times: int = 1) -> str:
    return (name + " ") * times

# B: optional return
def find_index(items: list, target) -> ???:
    """Return index of target or None if not found."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

# C: union types
def stringify(value: ???) -> str:
    """Accept int, float, or str. Return str."""
    return str(value)

# D: callable argument
def apply_twice(func: ???, value: float) -> float:
    return func(func(value))

# E: generic return (the result type matches the input type)
T = TypeVar("T")
def first(items: ???) -> ???:
    """Return first element of any list."""
    return items[0]

# F: dict with known structure
def make_training_summary(
    epoch: int,
    train_loss: float,
    val_loss: float,
    metrics: ???,      # dict mapping metric name to float value
) -> ???:             # same dict type
    return {"epoch": epoch, "train_loss": train_loss, "val_loss": val_loss, **metrics}

# G: iterator/generator
def positive_integers() -> ???:
    n = 1
    while True:
        yield n
        n += 1
```

---

**Exercise 6.2** — Type hints for class methods. Annotate this entire class:

```python
class RunningStats:
    """Tracks running mean and variance using Welford's online algorithm."""

    def __init__(self):
        self._count = 0
        self._mean = 0.0
        self._M2 = 0.0    # sum of squared deviations

    def update(self, value) -> None:
        """Add a new observation."""
        self._count += 1
        delta = value - self._mean
        self._mean += delta / self._count
        delta2 = value - self._mean
        self._M2 += delta * delta2

    @property
    def count(self):
        return self._count

    @property
    def mean(self):
        if self._count == 0:
            return None
        return self._mean

    @property
    def variance(self):
        if self._count < 2:
            return None
        return self._M2 / (self._count - 1)

    @property
    def std(self):
        v = self.variance
        if v is None:
            return None
        return v ** 0.5

    def reset(self) -> None:
        self._count = 0
        self._mean = 0.0
        self._M2 = 0.0
```

Add correct type hints to every method and property. Properties that might return None should use `Optional[float]`.

Then verify it works:
```python
stats = RunningStats()
for x in [2, 4, 4, 4, 5, 5, 7, 9]:
    stats.update(x)
assert stats.count == 8
assert abs(stats.mean - 5.0) < 1e-10
assert abs(stats.variance - 4.0) < 1e-10
assert abs(stats.std - 2.0) < 1e-10
print("RunningStats: all assertions passed")
```

---

# SECTION 7 — File I/O and Modules

---

**Exercise 7.1** — File operations: the correct patterns.

```python
import json
import csv
import os
from pathlib import Path

# Pattern 1: always use context managers for file I/O
def write_json(data: dict, path: str) -> None:
    """Write dict to JSON file. Create parent directories if needed."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def read_json(path: str) -> dict:
    """Read JSON file. Raise FileNotFoundError with informative message."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path!r}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Pattern 2: pathlib for path manipulation (modern Python)
def find_all_python_files(root_dir: str) -> list[Path]:
    """Recursively find all .py files under root_dir."""
    return list(Path(root_dir).rglob("*.py"))

def get_experiment_path(base_dir: str, experiment_name: str, run_id: int) -> Path:
    """Return path like: base_dir/experiment_name/run_001/"""
    return Path(base_dir) / experiment_name / f"run_{run_id:03d}"

# Pattern 3: reading CSV without pandas
def read_csv_as_dicts(path: str) -> list[dict]:
    """Read CSV into list of dicts (one dict per row)."""
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(rows: list[dict], path: str, fieldnames: list[str] = None) -> None:
    """Write list of dicts to CSV."""
    if not rows:
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Exercise: use the functions above to:
# 1. Write a config dict to "output/config.json"
# 2. Read it back and verify it matches
# 3. Write a list of experiment results to "output/results.csv"
# 4. Read it back and verify

config = {"lr": 0.001, "epochs": 100, "hidden": [128, 64]}
write_json(config, "output/config.json")
loaded = read_json("output/config.json")
assert loaded == config

results = [
    {"epoch": 1, "train_loss": 0.95, "val_loss": 0.97},
    {"epoch": 2, "train_loss": 0.82, "val_loss": 0.85},
    {"epoch": 3, "train_loss": 0.71, "val_loss": 0.74},
]
write_csv(results, "output/results.csv")
loaded_results = read_csv_as_dicts("output/results.csv")
assert len(loaded_results) == 3
```

---


# SECTION 8 — Git and GitHub Drills

*Not Python exercises — structured Git tasks, done in order, in a real
terminal, in a real repo. Use the commit convention from `docs/GIT_GUIDE.md`
(scoped, e.g. `feat(p0/python): ...`) for all commits below, not the
unscoped examples originally shown in some of these drills.*

---

## 8.1 — Repository Setup (do this now, before the projects)

Set up a repository for your Phase 0 exercises. This repo will hold all your Python and NumPy exercise work.

```bash
# Step 1: Create the repo locally
mkdir phase0_exercises
cd phase0_exercises
git init

# Step 2: Configure identity (if not done globally)
git config user.name "Your Name"
git config user.email "your@email.com"

# Step 3: Create initial structure
mkdir -p src/exercises src/projects tests notebooks docs
touch README.md .gitignore requirements.txt

# Step 4: Write .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/
dist/
build/
.DS_Store
Thumbs.db
.ipynb_checkpoints/
*.pkl
*.pt
*.pth
output/
data/
.env
EOF

# Step 5: Write README.md
# (Write a proper README — at least: what this repo is, how to install, what's inside)

# Step 6: Initial commit
git add .
git commit -m "chore: initial project scaffolding"

# Step 7: Create a GitHub repo (do this on github.com), then:
git remote add origin https://github.com/YOURUSERNAME/phase0_exercises.git
git branch -M main
git push -u origin main
```

Verify: open github.com and confirm your repo is there with the commit.

---

## 8.2 — The Daily Git Workflow

For every exercise section you complete, follow this exact workflow:

```bash
# Check current state before starting
git status          # should be clean before you start
git log --oneline   # see where you are

# Work on exercises (write code, test it, fix it)
# ...

# When the section is done:
git status          # see what changed
git diff            # see the actual changes

# Stage and commit
git add src/exercises/section2_comprehensions.py
git commit -m "feat: complete section 2 — comprehensions and functional patterns"

# Or stage all at once:
git add .
git commit -m "feat: complete section 3 — functions in depth"

git push   # push to GitHub
```

Practice writing good commit messages. Run `git log --oneline` after every commit and make sure each message is informative.

---

## 8.3 — Branching Workflow

All project work (Projects 1, 2, 3 below) should be done on a branch.

```bash
# Create a branch for Project 1
git checkout -b project/config-manager

# Work on the project
# ...commit frequently...

# Push the branch to GitHub
git push -u origin project/config-manager

# When the project is complete, merge back to main
git checkout main
git merge project/config-manager

# Delete the feature branch
git branch -d project/config-manager
git push origin --delete project/config-manager

# Tag the completed project
git tag -a v1.0-config-manager -m "Complete Config Manager project"
git push origin --tags
```

---

## 8.4 — Understanding the Git Object Model

These commands help you understand what Git is actually storing:

```bash
# Inspect the last commit
git show HEAD              # full diff of last commit
git show HEAD --stat       # just the file summary
git show HEAD:README.md    # show a specific file at HEAD

# Look at the git log
git log --oneline          # compact
git log --oneline --graph  # visual branch graph
git log --oneline --all    # all branches

# Compare commits
git diff HEAD~1 HEAD       # changes between last two commits
git diff main project/config-manager   # compare branches

# Unstaging and undoing
git add src/bad_file.py
git reset HEAD src/bad_file.py    # unstage without losing changes
git checkout -- src/bad_file.py   # discard changes in file (caution!)

# Stash: save work without committing
git stash              # save current changes
git stash pop          # restore saved changes
git stash list         # see all stashes
```

---

## 8.5 — .gitignore Drills

Create these files in your repo, then verify that `.gitignore` is excluding the right things:

```bash
# Create files that should be ignored
mkdir -p data output __pycache__
touch data/training.csv
touch output/model.pt
touch __pycache__/module.cpython-311.pyc
touch secret.env

# Create files that should NOT be ignored
touch src/exercises/real_code.py
touch tests/test_something.py
touch README.md

# Check what git sees
git status

# Expected: real_code.py, test_something.py, README.md appear as untracked
# Expected: data/, output/, __pycache__/, secret.env do NOT appear

# If something that should be ignored is already tracked:
# git rm --cached filename   (removes from git tracking without deleting the file)
```

---

## 8.6 — Reading Git History

```bash
# Find when a specific line was changed
git log -S "def some_function"    # find commits that added or removed this text
git log --all --full-history -- "src/exercises/section3.py"  # commits touching a file

# Blame: who wrote each line
git blame src/exercises/section2_comprehensions.py

# Revert: undo a commit by creating a new commit
git revert HEAD        # undo last commit (safe — does not rewrite history)
git revert abc123      # undo a specific commit by hash
```

Drill: make a "mistake" commit (add a file with a deliberate error), then revert it with `git revert`. Look at the log and understand what happened.

---

# COMPLETION CHECKLIST

Be honest. These are standards, not aspirations.

## Fundamentals
- [ ] Can explain the difference between mutation and rebinding with a concrete example
- [ ] Knows the mutable default argument trap and always uses None as default for mutable args
- [ ] Understands shallow vs deep copy and when each is needed
- [ ] Never uses `is` to compare values (only for None checks)

## Comprehensions and Functional Patterns
- [ ] Can convert any for-loop to a list comprehension without thinking about it
- [ ] Uses dict and set comprehensions naturally
- [ ] Uses generator expressions instead of list comprehensions when intermediate results are not needed
- [ ] Understands the late-binding closure trap and how to fix it

## Functions
- [ ] Can write functions with *args, **kwargs, keyword-only arguments, and positional-only arguments
- [ ] Can write a decorator from scratch including functools.wraps
- [ ] Can write a decorator factory (a decorator that takes arguments)
- [ ] Can write closures using nonlocal correctly
- [ ] Can write generator functions and chain them into pipelines

## OOP
- [ ] Can implement all relevant dunder methods for a custom container class
- [ ] Uses @property with getters and setters correctly
- [ ] Uses @classmethod for alternative constructors correctly
- [ ] Uses @staticmethod for utility functions that don't need self or cls
- [ ] Can define abstract base classes with @abstractmethod
- [ ] Can implement context managers with __enter__ and __exit__
- [ ] Understands when to inherit vs when to compose

## Error Handling and Type Hints
- [ ] Has a custom exception hierarchy in every project
- [ ] Always catches specific exceptions, never bare `except:` or `except Exception: pass`
- [ ] Uses logging instead of print in all project code
- [ ] Applies type hints to every function and method signature
- [ ] Knows the most common types: Optional, Union, List, Dict, Tuple, Callable, TypeVar

## Git
- [ ] Has a GitHub repo with at least 20 commits for this exercise set
- [ ] Every commit has a meaningful message with a proper prefix (feat/fix/refactor/test/docs/chore)
- [ ] Has used branching for project work and merged cleanly to main
- [ ] Knows git status, diff, log, add, commit, push, pull, branch, checkout, merge, stash, revert
- [ ] Has a correct .gitignore that excludes __pycache__, .venv, data files, and model checkpoints

Projects (Weather Tool, Data Pipeline, Linear Regression, NumPy Neural Net, and stretch) are tracked separately — see `docs/PHASE0_PROJECTS.md` and `phase0/README.md`.
