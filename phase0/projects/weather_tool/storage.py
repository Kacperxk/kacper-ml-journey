from .models import WeatherData
from pathlib import Path
from .exceptions import StorageError
import json


def save_records(records: list[WeatherData], path: str) -> None:
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump([x.to_dict() for x in records], f, indent=2)
    except OSError as e:
        raise StorageError(f"Failed saving file: {e}") from e


def load_records(path: str) -> list[WeatherData]:
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")
    try:
        with open(path) as f:
            return [WeatherData.from_dict(x) for x in json.load(f)]
    except json.JSONDecodeError as e:
        raise StorageError(f"Failed loading file: {e}") from e
