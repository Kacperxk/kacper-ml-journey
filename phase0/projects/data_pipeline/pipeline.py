from collections.abc import Iterable, Iterator, Callable
from .exceptions import PipelineError


class Pipeline:
    """Chainable, lazy wrapper around an iterable. Nothing is computed until the pipeline is iterated or collected."""

    def __init__(self, source: Iterable) -> None:
        self.source = source

    def __iter__(self) -> Iterator:
        return iter(self.source)

    def map(self, fn: Callable) -> "Pipeline":
        def inner():
            for x in self.source:
                yield fn(x)

        return Pipeline(inner())

    def filter(self, predicate: Callable) -> "Pipeline":
        def inner():
            for i, x in enumerate(self.source):
                try:
                    if predicate(x):
                        yield x
                except Exception as e:
                    raise PipelineError("filter", i, e) from e

        return Pipeline(inner())

    def batch(self, size: int) -> "Pipeline":
        pass


test1 = Pipeline([1, 2, 3]).map(lambda x: x + 2).filter(lambda x: x % 2 == 1)
it = iter(test1)
print(next(it))
print(next(it))
