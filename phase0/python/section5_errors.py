import logging


# Exercise 5.1


class DataError(Exception):
    """Base claa for all data-related errors"""
    pass

class FileFormatError(DataError):
    """Raised when a file has an unexpected format."""
    def __init__(self, path: str, expected: str, got: str):
        self.path = path
        self.expected = expected
        self.got = got
        super().__init__(f"File {path!r}: expected {expected}, got {got}")

class ColumnMissingError(DataError):
    """Raised when a required column is absent from the dataset"""
    def __init__(self, column: str, available: list[str]):
        self.column = column
        self.available = list(available)
        super().__init__(f"column: {column}, available: {available}")

class ShapeMismatchError(DataError):
    """Raised when array shapes are incompatible"""
    def __init__(self, expected: tuple, got: tuple, context: str = ""):
        self.expected = expected
        self.got = got
        self.context = context
        super().__init__(f"{f'{context}: ' if context else ''}Shape mismatch: expected {expected}, got {got}")

class ValidationError(DataError):
    """Raised when data fails validation checks"""
    pass


def load_and_validate(path: str, required_columns: list[str], expected_shape: tuple):
    """
    Load CSV-like data structure and validate it.
    Raise appropriate custom exeptions for each failure mode.
    """
    with open(path) as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        for col in required_columns:
            if col not in header:
                raise ColumnMissingError(col, header)

        shape_got = (len(lines) - 1, len(header))
        if shape_got != expected_shape:
            raise ShapeMismatchError(expected_shape, shape_got)

try:
    load_and_validate("nonexistent.csv", ["a", "b"], (100, 2))
except FileNotFoundError:
    print("Caught FileNotFoundError")

with open("data.csv", "w") as f:
    f.write("a,b\n1,2\n3,4\n")

try:
    load_and_validate("data.csv", ["missing_col"], (100, 2))
except ColumnMissingError as e:
    print(f"Missing column: {e.column}")
except DataError as e:
    print(f"General data error: {e}")

load_and_validate("data.csv", ["a", "b"], (2, 2))
print("Valid data.csv passed validation")

try:
    load_and_validate("data.csv", ["a", "b"], (100, 2))
    assert False, "Should raise ShapeMismatchError"
except ShapeMismatchError as e:
    print(f"Shape mismatch: expected {e.expected}, got {e.got}")



# Exercise 5.2


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)

def load_checkpoint(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        logger.error("Checkpoint not found %s", path)
        raise
    except json.JSONDecodeError as e:
        logger.error("Corrupt checkpoint %s: %s", path, e)
        raise ValueError(f"Checkpoint path {path!r} is corrupted") from e

def load_config(path: str) -> dict:
    defaults = {"lr": 0.001, "epochs": 10}
    try:
        with open(path) as f:
            import json
            config = json.load(f)
            logger.info("Loaded config from %s", path)
            return config
    except FileNotFoundError:
        logger.warning("Config not found at %s, using defaults", path)
        return defaults

def validate_config(config: dict) -> list[str]:
    """
    Return a list of all validation errors (not just the first one).
    Check: "lr" key present, is a float, and is >= 1.
           "epochs" key present, is an int, and is >= 1.
    """
    errors = []
    if "lr" not in config:
        msg = 'lr not in config'
        logger.error(msg)
        errors.append(msg)
    elif not isinstance(config["lr"], float):
        msg = 'lr is not an float'
        logger.error(msg)
        errors.append(msg)
    elif config["lr"] < 1:
        msg = 'lr is less than 1'
        logger.error(msg)
        errors.append(msg)

    if "epochs" not in config:
        msg = 'epochs not in config'
        logger.error(msg)
        errors.append(msg)
    elif not isinstance(config["epochs"], int):
        msg = 'epochs is not an int'
        logger.error(msg)
        errors.append(msg)
    elif config["epochs"] < 1:
        msg = 'epochs is less than 1'
        logger.error(msg)
        errors.append(msg)
    return errors

errors = validate_config({"lr": -0.001, "epochs": 0})
print(len(errors))
assert len(errors) == 2
for e in errors:
    print(f" Error: {e}")