from typing import Any, Optional
from abc import ABC, abstractmethod
import time
import logging
import os
import shutil
import tempfile
import json


# Exercise 4.1


class BoundedList:
    """
    A list-like container with maximum capacity.
    When full, adding items raises an OverflowError.
    """

    def __init__(self, max_size: int):
        self.max_size = max_size
        self._items = []

    def append(self, item) -> None:
        """Add item. Raise OverflowError if at capacity"""

        if self.is_full:
            raise OverflowError("Maximum list capacity reached")

        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int):
        return self._items[index]

    def __setitem__(self, index: int, value) -> None:
        self._items[index] = value

    def __delitem__(self, index: int) -> None:
        self._items.pop(index)

    def __contains__(self, item) -> bool:
        """Supports: 'x in _items'"""
        return item in self._items

    def __iter__(self):
        """Supports: 'for x in _items'"""

        return iter(self._items)

    def __repr__(self) -> str:
        return f"BoundedList({self._items}, max_size={self.max_size})"

    def __eq__(self, other) -> bool:
        """Equal if same contents and same max_size."""

        if not isinstance(other, BoundedList):
            return NotImplemented
        return self._items == other._items and self.max_size == other.max_size

    @property
    def is_full(self) -> bool:
        return len(self._items) >= self.max_size

    @property
    def remaining(self) -> int:
        """How many more items can be added"""

        return self.max_size - len(self._items)

bl = BoundedList(max_size=3)
bl.append(10)
bl.append(20)
bl.append(30)
assert len(bl) == 3
assert bl.is_full
assert bl.remaining == 0
assert bl[0] == 10
assert bl[-1] == 30
assert 30 in bl
assert 99 not in bl

try:
    bl.append(40)
    assert False, "Should have raised OverflowError"
except OverflowError:
    pass

values = list(bl)
assert values == [10, 20, 30]

bl[1] = 99
assert bl[1] == 99

del bl[0]
assert len(bl) == 2
assert bl.remaining == 1

a = BoundedList(3)
b = BoundedList(3)
a.append(1); b.append(1)
assert a == b

print("BoundedList: all tests passed")


# Exercise 4.2


class LearningRateScheduler:
    """
    Manages a learning rate for model training.
    Enforces constrains and tracks history.
    """

    def __init__(self, initial_lr: float, min_lr: float = 1e-6, max_lr: float = 1.0):

        if initial_lr < min_lr or initial_lr > max_lr:
            raise ValueError("Initial learning rate out of bounds")
        
        self._lr = initial_lr
        self.initial_lr = initial_lr
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.lr_history = [initial_lr]


    @property
    def lr(self) -> float:
        return self._lr

    @lr.setter
    def lr(self, value: float) -> None:

        if value < self.min_lr or value > self.max_lr:
            raise ValueError("Learning rate out of bounds")

        self._lr = value
        self.lr_history.append(value)

    @property
    def history(self) -> list:
        """All learning rate values seen so far (read-only)"""

        return self.lr_history.copy()

    @property
    def n_updates(self) -> int:
        """How many times the LR has been set (not counting initial)."""

        return len(self.lr_history) - 1

    def decay(self, factor: float) -> None:
        """Multiply current LR by factor. Clamp to min_lr if needed"""

        if self.lr * factor < self.min_lr:
            self.lr = self.min_lr
        else:
            self.lr = self.lr * factor
        

    def reset(self) -> None:
        """Reset to initial LR, clear history"""

        self._lr = self.initial_lr
        self.lr_history.clear()
        self.lr_history.append(self.initial_lr)

    def __repr__(self) -> str:
        return f"LRScheduler(lr={self.lr:.6f}, updates={self.n_updates})"

    
scheduler = LearningRateScheduler(initial_lr=0.01, min_lr=1e-5, max_lr = 0.1)
assert scheduler.lr == 0.01
assert scheduler.n_updates == 0

scheduler.lr = 0.001
assert scheduler.lr == 0.001
assert scheduler.n_updates == 1

try:
    scheduler.lr = 10.0
    assert False, "Should raise ValueError"
except ValueError:
    pass

scheduler.decay(0.5)
assert abs(scheduler.lr - 0.0005) < 1e-10

h = scheduler.history
h.append(999.0)
assert 999.0 not in scheduler.history

scheduler.reset()
assert scheduler.lr == 0.01
assert scheduler.n_updates == 0


# Exercise 4.3


class Dataset:
    """
    A simple supervised learning dataset.
    Multiple ways to construct it - this is the factory pattern.
    """

    def __init__(self, features: list[list[float]], labels: list[int], name: str = "unnamed"):
        if len(features) != len(labels):
            raise ValueError(f"features and labels must match: {len(features)} vs {len(labels)}")

        self._features = [list(f) for f in features]
        self._labels = list(labels)
        self.name = name
        self._n_features = len(features[0]) if features else 0

    @classmethod
    def from_dict(cls, data: dict, name: str = "unnamed") -> "Dataset":
        """
        Build from dict with keys "features" and "labels".
        Validate that the dict has the right structure.
        """
        if len(data) != 2: raise ValueError(f"Dict should have 2 keys, has {len(data)}")
        if "labels" not in data or "features" not in data: raise ValueError("Incorrect keys")

        return cls(data["features"], data["labels"], name)

    @classmethod
    def from_csv_string(cls, csv_text: str, label_col: int = -1, name: str = "unnamed") -> "Dataset":
        """
        Parse a CSV string where all columns are numeric.
        label_col: which column is not label (-1 = last column)
        ALL other columns are features.
        """
        features = []
        labels = []
        for sample in csv_text.strip().split('\n'):

            row = sample.split(',')

            labels.append(int(row.pop(label_col)))
            feature_row = [float(value) for value in row]
            features.append(feature_row)

        return cls(features, labels, name)

    @classmethod
    def from_json_string(cls, json_text: str) -> "Dataset":
        """Parse JSON string with structure {name: ..., "features": ..., "labels": ...}"""

        dict_data = json.loads(json_text)
        name = dict_data.pop("name")

        return cls.from_dict(dict_data, name)

    @staticmethod
    def validate_features(features: list[list[float]]) -> bool:
        """
        Return True if all feature vectors have the same length.
        Return False otherwise
        """

        if not features:
            return True

        vector_len = len(features[0])
        for vector in features:
            if len(vector) != vector_len:
                return False
        return True

    @staticmethod
    def encode_labels(labels: list) -> tuple[list[int], dict]:
        """
        Convert arbitrary labels (strings, etc.) to integers 0, 1, 2...
        Return (encoded_labels, label_to_int_mapping)
        """
        encoded_labels = []
        label_map = {}
        
        value = 0
        for key in labels:
            if key not in label_map:
                label_map[key] = value
                value += 1
            encoded_labels.append(label_map[key])

        return (encoded_labels, label_map)

    def __len__(self) -> int:
        return len(self._labels)

    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, n_samples={len(self)}, n_features={self._n_features})"

    def to_dict(self) -> dict:
        return {"name": self.name, "features": self._features, "labels": self._labels}

data = {
    "features": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    "labels": [0, 1, 0]
}

d = Dataset.from_dict(data, name="test")
assert len(d) == 3

csv_text = "1.0,2.0,0\n3.0,4.0,1\n5.0,6.0,0\n"
d2 = Dataset.from_csv_string(csv_text)
assert len(d2) == 3

json_text = '{"name": "j", "features": [[1.0, 2.0]], "labels": [1]}'
d3 = Dataset.from_json_string(json_text)
assert len(d3) == 1
assert d3.name == "j"

assert Dataset.validate_features([[1, 2], [3, 4], [5, 6]]) is True
assert Dataset.validate_features([[1, 2], [3, 4, 5]]) is False

encoded, mapping = Dataset.encode_labels(["cat", "dog", "cat", "fish"])
print(set(encoded))
assert encoded == [0, 1, 0, 2]
assert mapping["cat"] != mapping["dog"]


# Exercise 4.4


class Metric(ABC):
    """
    Abstract base class for evaluation metrics.
    Subclasses must implement compute and name().
    """
    higher_is_better = False

    def __init__(self):
        self._history: list[float] = []

    @property
    @abstractmethod
    def name(self) -> str:
        """The metric's name (e.g., 'accuracy, 'mse')"""
        pass

    @abstractmethod
    def compute(self, y_true: list, y_pred: list) -> float:
        """Compute the metric from true and predicted values."""
        pass

    def update(self, y_true: list, y_pred: list) -> float:
        """Compute and store the result in history"""
        value = self.compute(y_true, y_pred)
        self._history.append(value)
        return value

    @property
    def history(self) -> list[float]:
        return list(self._history)

    @property
    def best(self) -> Optional[float]:
        """Return best value from history, or None if history is empty"""
        if not self._history:
            return None

        if self.higher_is_better:
            return max(self._history)

        return min(self._history)

    def reset(self) -> None:
        self._history.clear()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

class Accuracy(Metric):
    """Fraction of correct predictions (for classification)"""
    higher_is_better = True

    @property
    def name(self) -> str:
        return "accuracy"

    def compute(self, y_true: list, y_pred: list) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have same length")
        return sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)

class MSE(Metric):
    """Mean squared Error (for regression)"""
    @property
    def name(self) -> str:
        return "mse"
    
    def compute(self, y_true: list, y_pred: list) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have same length")
        return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)

        
class MAE(Metric):
    """Mean Absolute Error (for regression)"""

    @property
    def name(self) -> str:
        return "mae"

    def compute(self, y_true: list, y_pred: list) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have same length")
        return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)
    
class MetricTracker:
    """
    Track multiple metrics across training epochs.
    """

    def __init__(self, *metrics: Metric):
        self.metrics = {m.name: m for m in metrics}

    def update(self, epoch: int, y_true: list, y_pred: list) -> dict[str, float]:
        """Update all metrics and return dict of current values."""
        return {name: m.update(y_true, y_pred) for name, m in self.metrics.items()}

    def summary(self) -> dict[str, dict[str, float]]:

        return {name: {"current": metric.history[-1], "best": metric.best}
                for name, metric in self.metrics.items()}

    def reset_all(self) -> None:
        for m in self.metrics.values():
            m.reset()

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

mse = MSE()
assert mse.best is None
v_mse = mse.update([1.0, 2.0, 3.0], [1.5, 2.5, 2.5])
assert abs(v_mse - 0.25) < 1e-10
assert mse.best == v_mse

tracker = MetricTracker(Accuracy(), MSE())
results = tracker.update(1, [0, 1, 1], [0, 1, 0])
assert "accuracy" in results
assert "mse" in results

mae = MAE()
v = mae.update([1.0, 2.0, 3.0], [1.5, 2.5, 2.5])
assert abs(v - 0.5) < 1e-10   # mean of |0.5|, |0.5|, |0.5|

summary = tracker.summary()
assert set(summary.keys()) == {"accuracy", "mse"}
assert summary["accuracy"]["current"] == results["accuracy"]
assert summary["accuracy"]["best"] == tracker.metrics["accuracy"].best
assert summary["mse"]["current"] == results["mse"]
assert summary["mse"]["best"] == tracker.metrics["mse"].best

print("Metric system: all tests passed")

# Exercise 4.5


class Timer:
    """
    Context manager that measures elapsed time.

    Usage:
        with Timer("forward pass") as t:
            do_computation()
        print(t.elapsed) # seconds
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
        return False

class SuppressErrors:
    """
    Context manager that suppresses specified exception types.

    Usage:
        with SuppressErrors(ValueError, KeyError):
            risky_operation() # if ValueError or KeyError, just continues
    """

    def __init__(self, *exception_types):
        self._exception_types = exception_types

    def __enter__(self) -> "SuppressErrors":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type == None: return False
        return issubclass(exc_type, self._exception_types)

class TempDirectory:
    """
    Context manager that creates a temporary directory on enter
    and deletes it (with all contents) on exit.
    """

    def __init__(self, prefix: str = "tmp_"):
        self.prefix = prefix
        self.path: Optional[str] = None

    def __enter__(self) -> str:
        self.path = tempfile.mkdtemp(prefix=self.prefix)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.path: shutil.rmtree(self.path)
        return False

with Timer("test", verbose=True) as t:
    time.sleep(0.05)
assert t.elapsed >= 0.04

with SuppressErrors(ValueError):
    int("not_a_number")
print("After suppressed error - code continues")

# with SuppressErrors(TypeError):
#     int("not_a_number") # ValueError - tested

with TempDirectory(prefix="test_") as tmpdir:
    test_file = os.path.join(tmpdir, "hello.txt")
    with open(test_file, "w") as f:
        f.write("hello")
    assert os.path.exists(test_file)

assert not os.path.exists(tmpdir) # cleaned
print("Context managers: all tests passed")