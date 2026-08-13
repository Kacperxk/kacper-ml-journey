from data_pipeline.pipeline import Pipeline
from data_pipeline.exceptions import PipelineError
from data_pipeline.sources import counter, read_jsonl
import tracemalloc
import random
import pytest
import json


def test_map_filter_collect():
    result = (
        Pipeline([1, 2, 3, 4, 5]).map(lambda x: x * 2).filter(lambda x: x > 4).collect()
    )
    assert result == [6, 8, 10]


def test_batch_and_take_infinite():
    result = Pipeline(counter()).batch(3).take(4).collect()

    assert len(result) == 4
    for batch in result:
        assert len(batch) == 3


def test_memory_efficiency_counter():
    result = Pipeline(counter()).map(lambda x: x + 2).map(lambda x: x * 3).take(100_000)
    tracemalloc.start()
    count = 0
    for _ in result:
        count += 1
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert count == 100000
    assert peak < 1_000_000


def test_shuffle_changes_order_and_stays_lazy():
    random.seed(42)
    original = list(range(20))
    result = Pipeline(original).shuffle(8).collect()
    assert result != original
    assert original == sorted(result)

    large_result = Pipeline(counter()).shuffle(20).take(100000)
    tracemalloc.start()
    count = 0
    for _ in large_result:
        count += 1
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert count == 100000
    assert peak < 1_000_000


def bad_function(x):
    if x == 3:
        raise ValueError("Bad value")
    return x


def test_map_error_propagation():
    result = Pipeline([1, 2, 3, 4, 5]).map(bad_function)
    with pytest.raises(PipelineError) as exc_info:
        result.collect()
    error = exc_info.value
    assert isinstance(error.original, ValueError)
    assert error.index == 2
    assert error.stage == "map"


def test_read_jsonl_memory_efficiency(tmp_path):
    path = f"{tmp_path}/large.jsonl"
    with open(path, "w") as f:
        for i in range(100000):
            f.write(json.dumps({"id": i, "value": i * 2}) + "\n")
    result = Pipeline(read_jsonl(path)).map(lambda x: x["value"])
    tracemalloc.start()
    count = 0
    for _ in result:
        count += 1
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert count == 100000
    assert peak < 1_000_000
