from collections.abc import Iterator
from pathlib import Path
import json


def counter(start: int = 0) -> Iterator[int]:
    current = start
    while True:
        yield current
        current += 1


def read_jsonl(path: str) -> Iterator[dict]:
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)
