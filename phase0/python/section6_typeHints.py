from typing import Any, Callable
from collections.abc import Iterator


# Exercise 6.1


def greet(name: str, times: int = 1) -> str:
    return (name + " ") * times

# Optional return
def find_index(items: list, target: Any) -> int | None:
    """Return index of target or None if not found."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

# Union types
def stringify(value: int | float | str) -> str:
    """Accept int, float, or str. Return str."""
    return str(value)

# callable argument
def apply_twice(func: Callable[[float], float], value: float) -> float:
    return func(func(value))

# generic return
def first[T](items: list[T]) -> T:
    """Return first element of any list."""
    return items[0]

# dict with known structure
def make_training_summary(
    epoch: int,
    train_loss: float,
    val_loss: float,
    metrics: dict[str, float],
) -> dict[str, float]:
    return {"epoch": epoch, "train_loss": train_loss, "val_loss": val_loss, **metrics}

# iterator/generator
def positive_integers() -> Iterator[int]:
    n = 1
    while True:
        yield n
        n += 1

assert greet("Ada", 2) == "Ada Ada "
assert find_index([1, 2, 3], 2) == 1
assert find_index([1, 2, 3], 9) is None
assert stringify(3.14) == "3.14"
assert apply_twice(lambda x: x + 1, 5) == 7
assert first([10, 20, 30]) == 10
assert make_training_summary(1, 0.5, 0.6, {"acc": 0.9}) == {
    "epoch": 1, "train_loss": 0.5, "val_loss": 0.6, "acc": 0.9,
}
gen = positive_integers()
assert next(gen) == 1
assert next(gen) == 2
print("Exercise 6.1: sanity checks passed")


# Exercise 6.2


class RunningStats:
    """Tracks running mean and variance using Welford's online algorithm."""

    def __init__(self) -> None:
        self._count: int = 0
        self._mean: float = 0.0
        self._M2: float = 0.0    # sum of squared deviations

    def update(self, value: int | float) -> None:
        """Add a new observation."""
        self._count += 1
        delta: float = value - self._mean
        self._mean += delta / self._count
        delta2: float = value - self._mean
        self._M2 += delta * delta2

    @property
    def count(self) -> int:
        return self._count

    @property
    def mean(self) -> float | None:
        if self._count == 0:
            return None
        return self._mean

    @property
    def variance(self) -> float | None:
        if self._count < 2:
            return None
        return self._M2 / (self._count - 1)

    @property
    def std(self) -> float | None:
        v = self.variance
        if v is None:
            return None
        return v ** 0.5

    def reset(self) -> None:
        self._count = 0
        self._mean = 0.0
        self._M2 = 0.0

stats = RunningStats()
for x in [2, 4, 4, 4, 5, 5, 7, 9]:
    stats.update(x)
assert stats.count == 8
assert abs(stats.mean - 5.0) < 1e-10
assert abs(stats.variance - 4.571428571428571) < 1e-10
assert abs(stats.std - 2.138089935299395) < 1e-10
print("RunningStats: all assertions passed")