# Phase 0 Projects

Four core projects, done in order, plus optional stretch projects if there's time left before the deadline. Target date for all of Phase 0 (concepts + drills + projects): **September 27, 2026**.

---

## Core Projects (do these, in order)

### Project 1 — CLI Weather Tool

**Focus:** OOP, custom exceptions, external API integration, file I/O, `argparse`, logging, git workflow
**Time:** ~10-14 hours

A command-line tool that fetches real weather data from the [Open-Meteo API](https://open-meteo.com/) (free, no API key) for one or more cities, analyzes it, and persists results to disk. Open-Meteo's forecast endpoint takes latitude/longitude, not city names, so the tool also needs a geocoding step first — Open-Meteo provides a separate free geocoding endpoint for resolving a city name to coordinates.

This is the one pure software-engineering project in Phase 0 — OOP, a real external API, custom error handling, file persistence, and a real git history, all in one place.

#### Structure

Rough file breakdown — how you split logic within each file is yours to decide:

```
weather_tool/
├── __init__.py     # marks this folder as a package
├── exceptions.py   # custom exception hierarchy
├── models.py       # WeatherData — one weather observation/forecast point
├── fetcher.py      # WeatherFetcher — talks to the Open-Meteo API
├── analyzer.py     # WeatherAnalyzer — stats and comparisons across records
├── storage.py      # save/load records to/from disk
└── cli.py          # argparse entry point
```

#### `exceptions.py`

```python
class WeatherError(Exception):
    """Base exception for all errors raised by this tool."""

class APIError(WeatherError):
    """Raised when a request to the Open-Meteo API fails (network error, timeout, non-2xx response)."""

class CityNotFoundError(WeatherError):
    """Raised when a city name can't be resolved to coordinates via geocoding."""

class ParseError(WeatherError):
    """Raised when an API response is missing expected fields or can't be parsed into a WeatherData."""
```

#### `models.py`

```python
class WeatherData:
    """One weather observation or forecast point, for a single city and date."""

    city: str
    date: str
    temperature_c: float
    humidity_pct: float
    wind_speed_kmh: float
    precipitation_mm: float

    @property
    def temperature_f(self) -> float:
        """Temperature converted to Fahrenheit."""

    def to_dict(self) -> dict:
        """Serialize to a plain, JSON-safe dict."""

    @classmethod
    def from_dict(cls, data: dict) -> "WeatherData":
        """Reconstruct a WeatherData from a dict produced by to_dict()."""
```

#### `fetcher.py`

```python
class WeatherFetcher:
    """Fetches weather data from the Open-Meteo API."""

    def __init__(
        self,
        weather_url: str = "https://api.open-meteo.com/v1",
        geocoding_url: str = "https://geocoding-api.open-meteo.com/v1",
    ) -> None:
        """Store the two API base URLs used for requests — Open-Meteo splits weather and geocoding across separate subdomains."""

    def geocode(self, city: str) -> tuple[float, float]:
        """Resolve a city name to (latitude, longitude). Raises CityNotFoundError if no match is found."""

    def get_current(self, city: str) -> WeatherData:
        """Fetch current weather conditions for a city. Raises APIError or ParseError on failure."""

    def get_forecast(self, city: str, days: int = 3) -> list[WeatherData]:
        """Fetch a multi-day forecast for a city, one WeatherData per day. Raises APIError or ParseError on failure."""
```

#### `analyzer.py`

```python
class WeatherAnalyzer:
    """Computes stats and comparisons across a collection of WeatherData records."""

    def __init__(self, records: list[WeatherData]) -> None:
        """Store the records this analyzer operates on."""

    def min_temperature(self) -> WeatherData:
        """Return the record with the lowest temperature."""

    def max_temperature(self) -> WeatherData:
        """Return the record with the highest temperature."""

    def average_temperature(self, city: str | None = None) -> float:
        """Return the mean temperature across all records, optionally filtered to one city."""

    def compare_cities(self) -> dict[str, float]:
        """Return each city's average temperature, keyed by city name."""
```

#### `storage.py`

```python
def save_records(records: list[WeatherData], path: str) -> None:
    """Write a list of WeatherData records to a JSON file."""

def load_records(path: str) -> list[WeatherData]:
    """Read a list of WeatherData records back from a JSON file."""
```

#### `cli.py`

```python
def main() -> None:
    """Parse CLI arguments and dispatch to the requested command."""
```

The CLI needs at least these commands: fetch and display current weather for a city; fetch and display a forecast for a city; save fetched results to a file; load saved records and display stats/comparison across cities. Exact argument names and subcommand layout are yours to design.

**Done when:** the CLI works end-to-end for at least 2 cities (current weather and forecast), an invalid city name or API failure produces a clean error message with no raw traceback, fetched data can be saved to and reloaded from disk without loss, the stats/comparison command produces correct output across saved cities, and the git history has 10+ meaningful commits.

---

### Project 2 — Data Pipeline

**Focus:** generators, iterators, memory-efficient streaming, error handling
**Time:** ~6-7 hours

A chainable, lazy `Pipeline` class for processing data streams too large to fit in memory — the same pattern used for streaming ML training data. Every transformation stays lazy until the pipeline is iterated or collected, including when reading from a real file far larger than could reasonably be loaded at once.

#### Structure

Rough file breakdown — how you split logic within each file is yours to decide:

```
data_pipeline/
├── __init__.py
├── exceptions.py   # PipelineError
├── sources.py      # counter(), read_jsonl() — lazy data sources
├── pipeline.py     # Pipeline — chainable, lazy transformations
└── tests/
    └── test_pipeline.py   # the required test scenarios (pytest)
```

#### `exceptions.py`

```python
class PipelineError(Exception):
    """Raised when a pipeline stage fails processing an item."""

    def __init__(self, stage: str, index: int, original: Exception) -> None:
        """Store which stage and item index failed, and the original exception."""
```

#### `sources.py`

```python
def counter(start: int = 0) -> Iterator[int]:
    """Infinite generator yielding start, start+1, start+2, ... Used to prove pipeline operations never materialize the full source."""

def read_jsonl(path: str) -> Iterator[dict]:
    """Lazily yield parsed JSON objects from a JSONL file (one JSON object per line), one line at a time — never loads the whole file into memory."""
```

#### `pipeline.py`

```python
class Pipeline:
    """Chainable, lazy wrapper around an iterable. Nothing is computed until the pipeline is iterated or collected."""

    def __init__(self, source: Iterable) -> None:
        """Wrap a source iterable or generator."""

    def __iter__(self) -> Iterator:
        """Make the pipeline itself iterable."""

    def map(self, fn: Callable) -> "Pipeline":
        """Return a new Pipeline applying fn to each item, lazily. If fn raises on an item, raise PipelineError with the stage name, item index, and original exception."""

    def filter(self, predicate: Callable) -> "Pipeline":
        """Return a new Pipeline keeping only items where predicate(item) is True, lazily. If predicate raises on an item, raise PipelineError with the stage name, item index, and original exception."""

    def batch(self, size: int) -> "Pipeline":
        """Return a new Pipeline yielding lists of `size` consecutive items. The final batch may be smaller than size."""

    def shuffle(self, buffer_size: int) -> "Pipeline":
        """Return a new Pipeline that shuffles items using a fixed-size buffer, so shuffling never requires materializing the full source."""

    def take(self, n: int) -> "Pipeline":
        """Return a new Pipeline yielding only the first n items."""

    def collect(self) -> list:
        """Materialize the pipeline into a list. Terminal operation — defeats the memory-efficiency purpose, use only for small results or testing."""
```

**Required test scenarios** (`tests/test_pipeline.py`, pytest):
1. Basic pipeline — `map` + `filter` + `collect` on a small in-memory list produces the correct result.
2. `batch` + `take` — chaining both on an infinite `counter()` source produces the correct number of correctly-shaped batches without hanging.
3. Memory efficiency — using `tracemalloc`, confirm peak memory stays low while processing a `counter()` source far larger than available memory would allow if materialized.
4. Shuffle buffer — confirm `shuffle()` changes item order without requiring the full source to be materialized.
5. Error propagation — an item that makes `map()`'s function raise surfaces as a `PipelineError` with the correct stage, index, and original exception attached.
6. Real file streaming — build a pipeline from `read_jsonl()` on a large generated JSONL file, apply at least one transformation, and confirm memory stays low via `tracemalloc` despite the file's size.

**Done when:** all six test scenarios pass, `pytest` runs clean with no warnings, and the pipeline never materializes a full source in memory except inside `collect()`.

---

### Project 3 — Linear Regression from Scratch (with visualization)
**Focus:** NumPy vectorization, gradient descent, math-to-code translation
**Time:** ~1.5 weeks

Build a `LinearRegression` class in pure NumPy, in stages:
1. Closed-form OLS solution (`np.linalg.lstsq`, not `inv` — more stable)
2. Batch gradient descent
3. Mini-batch gradient descent
4. Ridge regression (L2 regularization, don't regularize the bias term)

Then visualize: loss curves for batch vs mini-batch GD on the same plot, predictions-vs-truth scatter, weight convergence over epochs, and compare **vanilla GD, momentum, and Adam** on the ill-conditioned toy function `f(x,y) = x² + 5y²`, showing Adam converges faster. Test the final class on both synthetic data (recover known weights) and a real dataset (California Housing via sklearn — expect R² ~0.5–0.7).

**Done when:** gradient descent matches OLS within 0.01 on toy data, all plots exist with clear labels, code runs correctly on California Housing.

---

### Project 4 — NumPy Neural Network (capstone)
**Focus:** full forward/backward pass, gradient checking, mini-batch training
**Time:** ~6–10 hours

A `TwoLayerNet` class (`Linear → ReLU → Linear → Softmax`, cross-entropy loss) implemented entirely in NumPy, including manual backward pass via the chain rule. Trained with mini-batch SGD on synthetic MNIST-style data. Must pass a numerical gradient check (`gradient_check` function, relative error < 1e-4) before you trust the training results.

This is the Phase 0 capstone and directly sets up Phase 2's PyTorch/backprop work — it fully replaces the need for the two "stretch" tensor-wrapper projects below, which cover the same ground at lower depth.

**Done when:** loss ≈ log(10) ≈ 2.3 at initialization, gradient check passes, validation accuracy exceeds 60% after 30 epochs, training curves plotted.

---

## Optional Stretch (only if you finish core projects with time to spare before Sept 27)

Do these in this priority order if you have time. Skip them entirely if you don't — none of them teach something the 4 core projects don't already cover, they just go deeper or practice the same skill in a different shape.

1. **Data Preprocessing Engine** (`StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `train_test_split` from scratch in NumPy). Reasonable to fold directly into Project 3's data-prep step instead of building standalone.
2. **Config Manager** (dot-notation config object with freezing, merging, diffing). Useful engineering pattern, lowest ML relevance of the stretch set.
3. **Mini Tensor Library** (`microtensor` — OOP wrapper around NumPy with dunder-method arithmetic). Largely superseded by Project 4 above.
4. **Mini ML Framework** (pure-Python, no NumPy, deliberately skips real backprop). Interesting for project-structure fluency but explicitly doesn't complete the learning loop (no real gradients) — lowest priority.

Ask if you want a fuller spec for any of these when you're ready to build one.

---

*Last updated: 2026-08-09*
