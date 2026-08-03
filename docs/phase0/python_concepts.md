# Phase 0 — Python Concepts

Part 1 of the Phase 0 teaching content (concepts, not drills — drills are in
`python_exercises.md` in this folder). Originally part of `phase0_complete.md`;
split out here per `docs/REPO_STRUCTURE.md`'s `docs/phase0/` structure.

---

# PART 1 — PYTHON

## Why This Level of Fluency Matters

You already know basic Python — enough to follow a tutorial. The target here is higher: when you are deep in implementing a model, Python should not be the obstacle. You should never be stopping to think "how do I write a class again." The language should feel like a transparent tool.

---

## 1.1 — Python Fundamentals You Must Have Solid

Before OOP, make these completely solid. Beginners often have them half-understood.

### Variables are labels, not boxes

In many languages, a variable is a box that holds a value. In Python, a variable is a label that points to an object. This distinction causes real bugs.

```python
a = [1, 2, 3]
b = a           # b is NOT a copy — both point to the SAME list

b.append(4)
print(a)        # [1, 2, 3, 4] — a changed too!

# To actually copy:
c = a.copy()
c.append(5)
print(a)        # [1, 2, 3, 4] — a did NOT change
```

This causes confusing bugs in ML code constantly. When you pass an array to a function and it "unexpectedly" changes outside the function, this is why.

### Mutability

- **Immutable:** `int`, `float`, `str`, `tuple` — when you "change" them, Python creates a new object
- **Mutable:** `list`, `dict`, `set`, and most class instances — modified in place

```python
# Integers are immutable
x = 5
y = x
y = y + 1      # creates a NEW int — does not change x
print(x)       # still 5

# Lists are mutable
a = [1, 2, 3]
b = a
b[0] = 99      # modifies the SAME list
print(a)       # [99, 2, 3]
```

### Functions are first-class objects

Functions can be passed as arguments, assigned to variables, returned from other functions. This is the foundation for decorators and closures.

```python
def greet(name):
    return f"Hello, {name}"

say_hello = greet              # assign to a variable
print(say_hello("Anna"))       # "Hello, Anna"

def apply(func, value):        # accept a function as an argument
    return func(value)

result = apply(greet, "Piotr") # "Hello, Piotr"
```

### Scope

Variables live in the scope where they are defined. Inner functions can read from outer scopes but not write to them without `nonlocal` or `global`.

```python
x = 10         # module-level

def outer():
    y = 20     # local to outer
    def inner():
        print(x)  # can read module-level
        print(y)  # can read outer's scope
    inner()

outer()
# print(y)    # NameError — y does not exist here
```

---

## 1.2 — OOP: Object-Oriented Programming

This is the most important Python topic for ML. Every neural network layer, every dataset class, every training loop configuration is a class. You must be completely comfortable here.

### What a class is and why it exists

A **class** is a blueprint for creating objects. An **object** is a specific instance made from that blueprint.

Without classes, representing related data is messy:

```python
# Without classes — scattered variables
student_name = "Michal"
student_grade = 4.5
student_courses = ["Math", "Python"]

def print_student(name, grade, courses):
    print(f"{name} | {grade} | {courses}")
```

With a class, the data and the behavior that belongs together stay together:

```python
class Student:
    def __init__(self, name, grade, courses):
        self.name = name
        self.grade = grade
        self.courses = courses

    def print_info(self):
        print(f"{self.name} | Grade: {self.grade} | Courses: {self.courses}")

student1 = Student("Michal", 4.5, ["Math", "Python"])
student2 = Student("Anna", 5.0, ["Statistics", "ML"])

student1.print_info()   # Michal | Grade: 4.5 | Courses: ['Math', 'Python']
student2.print_info()   # Anna | Grade: 5.0 | Courses: ['Statistics', 'ML']
```

### `__init__` and `self`

`__init__` is the constructor — it runs automatically when you create a new object. `self` is a reference to the specific object being created. When you write `self.name = name`, you are storing that value on this particular object.

```python
class Dog:
    def __init__(self, name, breed):   # runs when you write: Dog("Rex", "Lab")
        self.name = name               # stored ON this object
        self.breed = breed
        self.tricks = []               # every dog starts with no tricks

    def learn_trick(self, trick):
        self.tricks.append(trick)      # modifies THIS dog's list

    def show_off(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} knows nothing yet")

rex = Dog("Rex", "Labrador")    # __init__ runs, self = rex
rex.learn_trick("sit")
rex.learn_trick("shake")
rex.show_off()                  # Rex knows: sit, shake

buddy = Dog("Buddy", "Poodle") # completely separate object
buddy.show_off()                # Buddy knows nothing yet
```

`self` is passed automatically — you never type it when calling a method. `rex.learn_trick("sit")` is Python shorthand for `Dog.learn_trick(rex, "sit")`.

### Instance variables vs class variables

`self.x` inside a method = **instance variable** — each object has its own copy.
Variable in the class body (outside methods) = **class variable** — shared by ALL instances.

```python
class Counter:
    total = 0               # CLASS variable — shared by all Counters

    def __init__(self, name):
        self.name = name    # INSTANCE variable — unique to each Counter
        Counter.total += 1  # increment the shared count

c1 = Counter("first")
c2 = Counter("second")
c3 = Counter("third")

print(Counter.total)  # 3 — class variable
print(c1.name)        # "first" — instance variable
print(c2.name)        # "second"
```

### Methods: instance, class, and static

```python
class Temperature:
    scale = "Celsius"      # class variable

    def __init__(self, value):
        self.value = value

    # INSTANCE METHOD — receives the object via self
    def to_fahrenheit(self):
        return self.value * 9/5 + 32

    # CLASS METHOD — receives the CLASS itself via cls, not an instance
    # Use this for alternative constructors (creating objects in other ways)
    @classmethod
    def from_fahrenheit(cls, f_value):
        celsius = (f_value - 32) * 5/9
        return cls(celsius)   # creates and returns a new Temperature object

    # STATIC METHOD — no access to object or class
    # A regular function that logically belongs here
    @staticmethod
    def is_valid(value):
        return value >= -273.15

t = Temperature(100)
print(t.to_fahrenheit())               # 212.0
t2 = Temperature.from_fahrenheit(32)   # class method — no object needed to call
print(t2.value)                        # 0.0
print(Temperature.is_valid(-300))      # False
```

### Dunder (magic) methods

Dunder methods let your objects respond to Python's built-in syntax. Python calls them automatically — you never call them directly.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # What you see in a debugger or REPL — make it look like valid Python
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        # What print() shows — more human-friendly
        return f"({self.x}, {self.y})"

    def __len__(self):
        # len(v) — a 2D vector has 2 components
        return 2

    def __add__(self, other):
        # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # 3 * v — when the left side does not know how to handle this
        return self.__mul__(scalar)

    def __eq__(self, other):
        # v1 == v2
        return self.x == other.x and self.y == other.y

    def __getitem__(self, index):
        # v[0], v[1]
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError(f"Vector index {index} out of range")

    def __iter__(self):
        # for component in v:
        yield self.x
        yield self.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)          # (1, 2) — calls __str__
print(repr(v1))    # Vector(1, 2) — calls __repr__
print(len(v1))     # 2
print(v1 + v2)     # (4, 6) — calls __add__, returns a new Vector
print(v1 * 3)      # (3, 6)
print(3 * v1)      # (3, 6) — calls __rmul__
print(v1[0])       # 1
print(list(v1))    # [1, 2] — calls __iter__
```

The dunders you will use most in ML: `__init__`, `__repr__`, `__len__`, `__getitem__`, `__iter__`, `__call__`.

**`__call__`** is special — it lets you call an object like a function:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))    # 10 — calling the object like a function

# This is EXACTLY how PyTorch models work:
# model(input_tensor) calls model.__call__(input_tensor)
# which internally calls model.forward(input_tensor)
```

### Properties

A `@property` makes a method look like an attribute — no parentheses needed when accessing it. Use it to validate on write or compute on read.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # leading _ = "internal, don't touch directly"

    @property
    def radius(self):
        # runs when you ACCESS c.radius
        return self._radius

    @radius.setter
    def radius(self, value):
        # runs when you ASSIGN c.radius = something
        if value < 0:
            raise ValueError(f"Radius cannot be negative, got {value}")
        self._radius = value

    @property
    def area(self):
        # computed on the fly — no setter means read-only
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)    # 5 — calls getter (no parentheses)
print(c.area)      # 78.54 — computed on access
c.radius = 10      # calls setter — validates
# c.radius = -1    # raises ValueError
```

### Inheritance

A child class gets everything from a parent class and can extend or override it.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "woof")   # call parent's __init__ first!
        self.tricks = []

    def learn(self, trick):
        self.tricks.append(trick)

    def speak(self):
        # Override: add "!" to the parent's output
        return super().speak() + "!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")
    # No speak() override — inherits from Animal unchanged


dog = Dog("Rex")
cat = Cat("Luna")

print(dog.speak())    # "Rex says woof!" — overridden
print(cat.speak())    # "Luna says meow" — inherited
print(dog.name)       # "Rex" — inherited attribute
dog.learn("sit")
print(dog.tricks)     # ['sit']
print(repr(dog))      # "Dog(name='Rex')" — inherited __repr__
```

Always call `super().__init__()` in a child's `__init__`. Without it, the parent never sets up its attributes.

The pattern you will use constantly in ML:

```python
class BaseModel:
    """Defines the interface — what every model must have."""
    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward()")

    def predict(self, x):
        return self.forward(x)   # shared logic that every child gets for free


class LinearModel(BaseModel):
    def forward(self, x):
        # specific implementation
        pass

class TreeModel(BaseModel):
    def forward(self, x):
        # completely different implementation
        pass
```

Parent defines *what* must exist. Children define *how*. This is the foundation of PyTorch's `nn.Module`.

### A complete, realistic class

```python
class Dataset:
    """
    Holds labeled training data for supervised learning.

    Stores input features and output labels together, validates
    they match in size, and supports iteration and indexing.
    """

    def __init__(self, features: list, labels: list):
        if len(features) != len(labels):
            raise ValueError(
                f"features and labels must have same length, "
                f"got {len(features)} and {len(labels)}"
            )
        self._features = list(features)
        self._labels = list(labels)

    @property
    def size(self) -> int:
        """Number of samples in the dataset."""
        return len(self._features)

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, index: int):
        """Get a single (feature, label) pair by index."""
        return self._features[index], self._labels[index]

    def __iter__(self):
        """Iterate over all (feature, label) pairs."""
        for i in range(self.size):
            yield self._features[i], self._labels[i]

    def __repr__(self) -> str:
        return f"Dataset(size={self.size})"

    @classmethod
    def from_dict(cls, data: dict) -> "Dataset":
        """Build a Dataset from a dict with 'features' and 'labels' keys."""
        return cls(data["features"], data["labels"])

    def split(self, ratio: float = 0.8):
        """Split into train and test datasets."""
        if not 0 < ratio < 1:
            raise ValueError(f"ratio must be between 0 and 1, got {ratio}")
        n = int(self.size * ratio)
        train = Dataset(self._features[:n], self._labels[:n])
        test = Dataset(self._features[n:], self._labels[n:])
        return train, test


# Using it:
ds = Dataset([1, 2, 3, 4, 5], [0, 1, 0, 1, 1])
print(ds)               # Dataset(size=5)
print(len(ds))          # 5
print(ds[2])            # (3, 0)

for feature, label in ds:
    print(feature, label)

train, test = ds.split(0.6)
print(train, test)      # Dataset(size=3) Dataset(size=2)
```

---

## 1.3 — Functions: The Parts Most People Skip

### Default arguments — a classic trap

```python
# WRONG — the default list is created ONCE and shared across all calls
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]  surprise!
print(add_item(3))   # [1, 2, 3]  still growing

# CORRECT — use None, create fresh list each time
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

Always use `None` as the default for any mutable argument.

### *args and **kwargs

```python
def log(*args):
    # *args collects positional arguments into a tuple
    for i, val in enumerate(args):
        print(f"[{i}] {val}")

log(1, "hello", 3.14)
# [0] 1
# [1] hello
# [2] 3.14

def setup(**kwargs):
    # **kwargs collects keyword arguments into a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

setup(lr=0.001, epochs=10, batch_size=32)
# lr: 0.001
# epochs: 10
# batch_size: 32

# The ** unpacking operator — used constantly with config dicts in ML
config = {"lr": 0.001, "epochs": 10}
def train(lr, epochs): pass
train(**config)   # same as train(lr=0.001, epochs=10)
```

### Closures

A closure is a function that remembers variables from the scope where it was created, even after that scope is gone.

```python
def make_adder(n):
    def adder(x):
        return x + n   # 'n' is captured from make_adder's scope
    return adder

add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))    # 8
print(add10(3))   # 13
# add5 still remembers n=5 even though make_adder() has finished

# ML use case — learning rate schedulers:
def make_lr_scheduler(initial_lr, decay):
    def get_lr(step):
        return initial_lr * (decay ** step)
    return get_lr

schedule = make_lr_scheduler(0.01, 0.99)
print(schedule(0))    # 0.01
print(schedule(100))  # much smaller
```

### Decorators

A decorator wraps a function to add behavior before or after it, without modifying the function itself.

Step by step — how it actually works:

```python
# A wrapper that uppercases the result
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # call the original
        return str(result).upper()       # modify and return
    return wrapper

def greet(name):
    return f"hello, {name}"

# Apply manually:
greet = shout(greet)
print(greet("anna"))    # "HELLO, ANNA"
```

The `@` syntax is just cleaner shorthand for the same thing:

```python
@shout
def greet(name):
    return f"hello, {name}"
# Exactly equivalent to: greet = shout(greet)
```

A timer decorator you will actually use:

```python
import time
import functools

def timer(func):
    @functools.wraps(func)   # preserves original function name and docstring
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.3f}s")
        return result
    return wrapper

@timer
def train_epoch(model, data):
    time.sleep(0.5)   # simulating work
    return 0.42

loss = train_epoch(None, None)
# "train_epoch took 0.500s"
```

### Generators

A generator produces values one at a time using `yield`, instead of building a full list. Critical for large datasets.

```python
# Regular function — builds entire list in memory
def squares_list(n):
    return [i**2 for i in range(n)]

# Generator — produces one value at a time, pauses between each
def squares_gen(n):
    for i in range(n):
        yield i**2   # pauses here, gives back value, resumes next call

# Usage looks the same
for sq in squares_gen(5):
    print(sq)    # 0, 1, 4, 9, 16

# The difference at scale:
# sum(x**2 for x in range(1_000_000_000))   # generator: constant memory — fine
# sum([x**2 for x in range(1_000_000_000)]) # list: needs ~8GB — crashes

# Data batching pattern (used in every ML training loop):
def batch_generator(data, batch_size=32):
    for start in range(0, len(data), batch_size):
        yield data[start : start + batch_size]

for batch in batch_generator(huge_array):
    process(batch)
```

---

## 1.4 — Error Handling

### Try / Except properly

```python
def load_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError as e:
        print(f"No permission: {e}")
        return None
    finally:
        # ALWAYS runs — whether exception occurred or not
        print("load_file() finished")
```

The most common mistake: catching `Exception` too broadly. It hides real bugs:

```python
# BAD — silent failure, you never know something went wrong
try:
    result = complex_operation()
except Exception:
    pass

# GOOD — catch specific exceptions, re-raise everything else
try:
    result = complex_operation()
except FileNotFoundError as e:
    logger.error(f"Missing file: {e}")
    raise   # re-raise so the caller can handle it
```

### Custom exceptions

```python
class DataError(Exception):
    """Base class for data errors in this project."""
    pass

class ShapeError(DataError):
    """Raised when array shapes are incompatible."""
    pass

class RangeError(DataError):
    """Raised when values are out of acceptable range."""
    pass

def normalize(data):
    if len(data) == 0:
        raise RangeError("Cannot normalize empty array")
    return (data - data.mean()) / data.std()

# Callers can be specific about what they catch:
try:
    result = normalize(my_data)
except ShapeError:
    print("Fix the data shape")
except DataError:
    print("Some data problem occurred")
```

### Logging instead of print

`print` is for quick experiments. Real code uses `logging`:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)   # one per module

logger.debug("Detailed debug info: %s", value)   # hidden unless level=DEBUG
logger.info("Training started: %d samples", n)
logger.warning("Learning rate very high: %.4f", lr)
logger.error("Failed to load checkpoint: %s", path)

# Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
# Set level=INFO to hide DEBUG in production
```

---

## 1.5 — Type Hints

Type hints are documentation that static analysis tools can check automatically.

```python
from typing import Optional, List, Dict, Tuple, Callable

def train(
    data: List[float],
    labels: List[int],
    lr: float = 0.001,
    epochs: int = 10,
    callback: Optional[Callable[[float], None]] = None,
) -> Dict[str, List[float]]:
    history: Dict[str, List[float]] = {"loss": [], "accuracy": []}
    # ...
    return history
```

Most commonly used types:

```python
from typing import Optional, List, Dict, Tuple, Union

def find(key: str) -> Optional[int]:           # might return None
    pass

def mean(numbers: List[float]) -> float:
    pass

def bounds(data: List[float]) -> Tuple[float, float]:
    return min(data), max(data)

def process(x: Union[List, str]) -> str:       # accepts either type
    pass

# Python 3.10+ — cleaner syntax with |
def process(x: list | str) -> str:
    pass
```

Run `mypy your_file.py` to catch type errors before running the code. Install with `pip install mypy`.

---

## 1.6 — Project Structure and Modules

### Packages and `__init__.py`

A **module** is any `.py` file. A **package** is a folder containing `__init__.py`. Packages can contain other packages.

```
my_project/
├── __init__.py
├── models/
│   ├── __init__.py
│   └── linear.py
└── utils/
    ├── __init__.py
    └── metrics.py
```

`__init__.py` controls what gets exported from a package:

```python
# models/__init__.py
from .linear import LinearRegression
# Users can now write: from my_project.models import LinearRegression
# Instead of:          from my_project.models.linear import LinearRegression
```

### Imports

```python
# Absolute — full path from project root (use in scripts you run directly)
from my_project.utils.metrics import r_squared

# Relative — relative to current file's location (use inside packages)
from .metrics import r_squared        # same package
from ..models import LinearRegression  # parent package's models
```

### Standard ML project layout

```
project_name/
├── .git/
├── .gitignore
├── README.md
├── requirements.txt
│
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── dataset.py
│       │   └── preprocessing.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── linear.py
│       └── utils/
│           ├── __init__.py
│           └── metrics.py
│
├── tests/
│   ├── test_dataset.py
│   └── test_models.py
│
└── notebooks/
    └── exploration.ipynb
```

---

## 1.7 — Git

See `docs/GIT_GUIDE.md` for the full workflow and commit convention this repo
uses. (The original version of this section duplicated git guidance with a
different, unscoped commit convention — consolidated into `docs/GIT_GUIDE.md` to
avoid the two drifting apart.)

---

## 1.8 — Virtual Environments

Every project in its own environment. No exceptions.

```bash
# Create and activate
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# Install packages
pip install numpy matplotlib jupyter

# Save so others can reproduce
pip freeze > requirements.txt

# On another machine:
pip install -r requirements.txt

# Deactivate
deactivate
```

For ML work, conda handles CUDA libraries better:

```bash
conda create -n phase0 python=3.11
conda activate phase0
pip install numpy matplotlib jupyter
```

---

## 1.9 — Resources for Python

- *Fluent Python* by Luciano Ramalho — chapters 1, 9, 11, 17. The deepest treatment of Python's object model.
- Corey Schafer's OOP playlist on YouTube — 6 videos, very clear. Start here.
- Real Python (realpython.com) — excellent free articles on every topic above.
- *Pro Git* book — free at git-scm.com. Chapters 1–3 are all you need right now.
- Missing Semester of CS Education (MIT) — missing.csail.mit.edu. Git, shell, tooling in one week.

---
