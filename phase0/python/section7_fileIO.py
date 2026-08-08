import json
import csv
import os
from pathlib import Path


# Exercise 7.1


def write_json(data: dict, path: str) -> None:
    """Write dict to JSON file. Create parent directiories if needed"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def read_json(path: str) -> dict:
    """Read JSON file. Raise FileNotFoundError with informative message."""
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path) as f:
        return json.load(f)

def find_all_python_files(root_dir: str) -> list[Path]:
    """Recursively find all .py files under root_dir"""
    python_files = list(Path(root_dir).rglob("*.py"))

    return python_files

def get_experiment_path(base_dir: str, experiment_name: str, run_id: int) -> Path:
    """Return path like: base_dir/experiment_name/run_001/"""

    p = Path(base_dir) / experiment_name / f"run_{run_id:03d}"
    return p

def read_csv_as_dicts(path: str) -> list[dict]:
    """Read CSV into list of dicts (one dict per row)"""
    with open(path, newline="") as f:
        dicts = list(csv.DictReader(f))
        return dicts


def write_csv(rows: list[dict], path: str, fieldnames: list[str] | None = None) -> None:
    """Write list of dicts to CSV"""
    if not rows:
        raise ValueError(f"Rows cannot be empty, got {rows}")

    if not fieldnames:
        fieldnames = list(rows[0].keys())
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

config = {"lr": 0.001, "epochs": 100, "hidden": [128, 64]}

write_json(config, "output/config.json")
loaded = read_json("output/config.json")
assert config == loaded

results = [
    {"epoch": 1, "train_loss": 0.95, "val_loss": 0.97},
    {"epoch": 2, "train_loss": 0.82, "val_loss": 0.85},
    {"epoch": 3, "train_loss": 0.71, "val_loss": 0.74}
]
write_csv(results, "output/results.csv")
loaded_results = read_csv_as_dicts("output/results.csv")
assert len(loaded_results) == 3

py_files = find_all_python_files("output")
assert isinstance(py_files, list)
assert all(isinstance(p, Path) for p in py_files)

run_path = get_experiment_path("experiments", "resnet50", 3)
assert run_path == Path("experiments") / "resnet50" / "run_003"