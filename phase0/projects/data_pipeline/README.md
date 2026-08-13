# Data Pipeline

Chainable, lazy `Pipeline` class for streaming data transformations —
`map`, `filter`, `batch`, `shuffle`, `take`, `collect` — built entirely on
generators, so nothing is computed until the pipeline is iterated or
collected. Full spec: `docs/phase0/projects.md`.

## Usage

```python
from data_pipeline.pipeline import Pipeline
from data_pipeline.sources import counter, read_jsonl

Pipeline([1, 2, 3, 4, 5]).map(lambda x: x * 2).filter(lambda x: x > 4).collect()
Pipeline(counter()).batch(3).take(4).collect()
Pipeline(read_jsonl("data.jsonl")).map(lambda r: r["value"]).take(10).collect()
```

`counter()` is an infinite source, used to prove pipeline stages never
materialize the full input. `collect()` is the only method that does —
everything before it stays lazy.

## Structure

- `exceptions.py` — `PipelineError`, raised when a stage's function fails on an item
- `sources.py` — `counter()`, `read_jsonl()`: lazy data sources
- `pipeline.py` — `Pipeline`, the chainable transformation class
- `tests/test_pipeline.py` — the six required pytest scenarios

## Testing

```
cd phase0/projects
python -m pytest data_pipeline/tests/test_pipeline.py -v
```

Use `python -m pytest`, not bare `pytest` — `tests/` has no `__init__.py`,
so bare `pytest` won't resolve the `data_pipeline` import correctly.

---

*Status: done — see `phase0/README.md`.*
