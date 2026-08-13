from collections.abc import Iterable, Iterator, Callable
from .exceptions import PipelineError
import random


class Pipeline:
    """Chainable, lazy wrapper around an iterable. Nothing is computed until the pipeline is iterated or collected."""

    def __init__(self, source: Iterable) -> None:
        self.source = source

    def __iter__(self) -> Iterator:
        return iter(self.source)

    def map(self, fn: Callable) -> "Pipeline":
        def inner():
            for i, x in enumerate(self.source):
                try:
                    result = fn(x)
                except Exception as e:
                    raise PipelineError("map", i, e) from e
                yield result

        return Pipeline(inner())

    def filter(self, predicate: Callable) -> "Pipeline":
        def inner():
            for i, x in enumerate(self.source):
                try:
                    keep = predicate(x)
                except Exception as e:
                    raise PipelineError("filter", i, e) from e
                if keep:
                    yield x

        return Pipeline(inner())

    def batch(self, size: int) -> "Pipeline":
        def inner():
            chunk = []
            for item in self.source:
                chunk.append(item)
                if size == len(chunk):
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

        return Pipeline(inner())

    def shuffle(self, buffer_size: int) -> "Pipeline":
        def inner():
            it = iter(self.source)
            buffer = []
            for _ in range(buffer_size):
                try:
                    buffer.append(next(it))
                except StopIteration:
                    break
            while buffer:
                index = random.randrange(len(buffer))
                yield buffer[index]
                try:
                    buffer[index] = next(it)
                except StopIteration:
                    buffer.pop(index)

        return Pipeline(inner())


# test1 = Pipeline([1, 2, 3, 4, 5]).map(lambda x: x + 2).shuffle(2)
# for i in test1:
#     print(i)
