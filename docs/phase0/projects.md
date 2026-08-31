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
**Time:** ~1–1.5 weeks

Build a `LinearRegression` class in pure NumPy, in stages: closed-form OLS, batch gradient descent, mini-batch gradient descent, and optional L2 (ridge) regularization. Then visualize the results and compare three gradient descent variants — vanilla, momentum, and Adam — on a toy function. Test the final class on both synthetic data (recover known weights) and a real dataset (California Housing via sklearn).

**On L2 (ridge) regularization:** adds a penalty `alpha * sum(w**2)` to the MSE loss, discouraging large weights — this reduces overfitting by keeping the model simpler. Its gradient contribution is `2 * alpha * w`, added only to `w`'s gradient — never regularize the bias term `b`; penalizing it would just push every prediction toward zero rather than controlling model complexity.

**On the optimizer comparison — don't assume Adam wins.** Momentum and Adam formulas are in `math_concepts.md` 1.2, including a worked example. That example is worth re-reading closely before you build this: on a small, smooth, noise-free toy function, plain gradient descent with a well-tuned learning rate can match or beat both — adaptive methods earn their keep specifically when gradients are *noisy* (mini-batches) or the loss surface is large and messy (real neural networks). So run this comparison with **noisy gradients** (add small random noise to each gradient to simulate a mini-batch estimate, same as the `math_concepts.md` example) rather than clean ones, and go in ready to explain whatever you actually observe rather than expecting a predetermined winner.

#### Structure

Rough file breakdown — how you split logic within each file is yours to decide:

```
linear_regression/
├── __init__.py
├── model.py             # LinearRegression — fit (closed-form / batch / mini-batch / ridge), predict, score
├── optimizers.py        # vanilla_step, momentum_step, adam_step — shared by model.py and the toy-function comparison
├── metrics.py           # r_squared, mse
├── visualize.py         # the four required plots
└── run_experiments.py   # ties it together — synthetic data, California Housing, the optimizer comparison
```

#### `model.py`

```python
class LinearRegression:
    """Linear regression y = X @ w + b, fit via closed-form OLS or gradient descent."""

    def __init__(
        self,
        method: str = "gd",
        lr: float = 0.01,
        n_epochs: int = 100,
        batch_size: int | None = None,
        alpha: float = 0.0,
        optimizer: str = "vanilla",
        seed: int = 42,
    ) -> None:
        """
        method: "closed_form" (via np.linalg.lstsq — see the note on np.linalg.solve
                vs lstsq vs inv in numpy_concepts.md 1.7) or "gd" (gradient descent).
        batch_size: None = full-batch GD each epoch; an int = mini-batch GD.
        alpha: L2 penalty strength (0 = plain OLS/GD). See the ridge note above.
        optimizer: "vanilla", "momentum", or "adam" — only used when method="gd".
        Store hyperparameters. Initialize self.w, self.b as None (set during fit)
        and self.loss_history as an empty list.
        """

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Fit self.w (shape (n_features,)) and self.b (scalar). Dispatch to
        _fit_closed_form or _fit_gd based on self.method. Return self, so
        .fit(X, y).predict(...) chains (same convention as scikit-learn).
        """

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Return X @ self.w + self.b."""

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """R² of predictions on (X, y). See metrics.r_squared."""

    def _fit_closed_form(self, X: np.ndarray, y: np.ndarray) -> None:
        """Solve for w and b via np.linalg.lstsq. Account for the bias term
        (e.g. prepend a column of 1s to X before solving, then split the
        result back into w and b)."""

    def _fit_gd(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Run gradient descent for self.n_epochs epochs. Each epoch: split
        into batches of self.batch_size (one full-batch step if None),
        compute the MSE loss gradient w.r.t. w and b (shape-matching
        approach — see math_concepts.md 1.2), add the ridge penalty
        gradient to w's gradient only if self.alpha > 0, then step using
        self.optimizer (see optimizers.py). Append each epoch's average
        loss to self.loss_history.
        """
```

#### `optimizers.py`

```python
def vanilla_step(params: np.ndarray, grad: np.ndarray, lr: float) -> np.ndarray:
    """One vanilla GD step. See math_concepts.md 1.2."""

def momentum_step(
    params: np.ndarray, grad: np.ndarray, velocity: np.ndarray, lr: float, beta: float = 0.9
) -> tuple[np.ndarray, np.ndarray]:
    """One momentum step. Return (new_params, new_velocity). See math_concepts.md 1.2."""

def adam_step(
    params: np.ndarray, grad: np.ndarray, m: np.ndarray, v: np.ndarray, t: int,
    lr: float, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """One Adam step, with bias correction. Return (new_params, new_m, new_v). See math_concepts.md 1.2."""
```

These take plain arrays, not a `LinearRegression` specifically — reuse them both inside `model.py`'s `_fit_gd` (on `w`/`b`) and standalone in `run_experiments.py`'s toy-function comparison (on `[x, y]`).

#### `metrics.py`

```python
def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean squared error — the GD loss."""

def r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """R² = 1 - SS_res/SS_tot. Same function shown (docstring-only) in habits_and_tools.md — implement it for real here."""
```

#### `visualize.py`

```python
def plot_loss_curves(batch_losses: list[float], minibatch_losses: list[float]) -> None:
    """Both loss curves on one figure, labeled legend. Save to figures/loss_curves.png."""

def plot_predictions_vs_truth(y_true: np.ndarray, y_pred: np.ndarray) -> None:
    """Scatter of predicted vs true values plus a y=x reference line. Save to figures/predictions.png."""

def plot_weight_convergence(weight_history: np.ndarray) -> None:
    """Each weight's value over epochs, one figure. Save to figures/weight_convergence.png."""

def plot_optimizer_comparison(loss_histories: dict[str, list[float]]) -> None:
    """One line per optimizer (vanilla/momentum/adam), labeled legend. Save to figures/optimizer_comparison.png."""
```

`figures/` is already excluded in `.gitignore` — plots are regenerated by rerunning `run_experiments.py`, not committed.

#### `run_experiments.py`

```python
def main() -> None:
    """
    1. Generate synthetic data from known w, b plus small noise. Fit with
       method="closed_form" and method="gd", and verify both recover the
       known weights within tolerance.
    2. Fit with batch GD and mini-batch GD on the same synthetic data.
       Plot both loss curves together (plot_loss_curves).
    3. Add a couple of near-duplicate (collinear) features to the synthetic
       data. Fit with alpha=0 and alpha>0, and compare recovered weight
       magnitudes — ridge's weights should shrink relative to the
       unregularized fit.
    4. Load California Housing (sklearn.datasets.fetch_california_housing).
       Its features are on very different scales (income ~0-15, population
       ~3-35000, etc.) — GD will struggle or need a tiny learning rate
       without standardizing first (subtract mean, divide by std, per
       feature). Standardize, fit, report score() (R², expect roughly
       0.5-0.7). Plot predictions vs truth. (This is the "Data Preprocessing
       Engine" stretch item's StandardScaler, folded in here instead of
       built standalone — write it from scratch if you have time, or use
       sklearn.preprocessing.StandardScaler if you'd rather focus the time
       elsewhere this project.)
    5. Toy-function optimizer comparison: run vanilla GD, momentum, and
       Adam (via optimizers.py) on f(x, y) = x**2 + 5*y**2 starting from
       (3, 3), using noisy gradients (see the ridge/optimizer note above
       and math_concepts.md 1.2's worked example). Plot all three loss
       curves together and write a couple sentences on what you observe
       and why.
    """
```

**Done when:** closed-form and GD solutions agree with each other within 0.01 on synthetic data with known weights; batch vs mini-batch loss curves are plotted together with clear labels; ridge regression visibly shrinks weight magnitudes relative to the unregularized fit on collinear synthetic features; California Housing R² lands in the 0.5–0.7 range with a labeled predictions-vs-truth plot; the vanilla/momentum/Adam comparison on the toy function uses noisy gradients and is plotted, and you can explain in a sentence or two why the result came out the way it did.

---

### Project 4 — NumPy Neural Network (capstone)
**Focus:** full forward/backward pass, gradient checking, mini-batch training
**Time:** ~10–15 hours

A `TwoLayerNet` class (`Linear → ReLU → Linear → Softmax`, cross-entropy loss) implemented entirely in NumPy, including a manual backward pass via the chain rule. Trained with mini-batch SGD on synthetic classification data. Must pass a numerical gradient check before you trust any training results.

This is the Phase 0 capstone and directly sets up Phase 2's PyTorch/backprop work — it fully replaces the need for the Mini Tensor Library stretch project below, which covers the same ground at lower depth.

**On the backward pass:** the hard part is the very first gradient — from the loss back through softmax. Don't derive softmax's own Jacobian; `math_concepts.md` 1.3 has the combined softmax+cross-entropy shortcut (`d_logits = (probs - y_true) / n`), which is where backprop actually starts here. Everything after that (through the second Linear, through ReLU, through the first Linear) is the same shape-matching chain-rule pattern from `math_concepts.md` 1.2, just applied twice in sequence.

**On weight initialization:** use small random values for `W1`/`W2` (`randn * 0.01`, the same scale already used in `numpy_exercises.md` Ex 5.2) and zeros for `b1`/`b2`. Xavier/Kaiming initialization is real and better, but it's scoped to Phase 2 in `docs/ROADMAP.md` — simple fixed-scale init is enough to hit every target below.

#### Structure

Rough file breakdown — how you split logic within each file is yours to decide:

```
numpy_neural_net/
├── __init__.py
├── layers.py            # relu, relu_backward, softmax, cross_entropy
├── model.py              # TwoLayerNet — forward, backward, predict, gradient_check
├── train.py               # mini-batch SGD training loop
├── visualize.py             # training curves
└── run_experiments.py        # synthetic data, gradient check, training, plotting
```

#### `layers.py`

```python
def relu(x: np.ndarray) -> np.ndarray:
    """max(0, x), elementwise."""

def relu_backward(dout: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Backprop through relu: dout where x > 0, else 0. Same drelu/dz logic as
    math_concepts.md 1.2's scalar chain-rule example, applied elementwise."""

def softmax(logits: np.ndarray) -> np.ndarray:
    """Numerically stable softmax along the last axis. See math_concepts.md 1.3."""

def cross_entropy(y_true_onehot: np.ndarray, probs: np.ndarray) -> float:
    """Mean cross-entropy loss. See math_concepts.md 1.3."""
```

#### `model.py`

```python
class TwoLayerNet:
    """Linear -> ReLU -> Linear -> Softmax, trained with cross-entropy loss."""

    def __init__(self, n_features: int, n_hidden: int, n_classes: int, seed: int = 42) -> None:
        """Initialize W1 (n_features, n_hidden), b1 (n_hidden,), W2 (n_hidden,
        n_classes), b2 (n_classes,). See the weight initialization note above."""

    def forward(self, X: np.ndarray) -> tuple[np.ndarray, dict]:
        """z1 = X@W1+b1, a1 = relu(z1), z2 = a1@W2+b2, probs = softmax(z2).
        Return (probs, cache) — cache holds whatever backward() will need
        (X, z1, a1, z2, probs at minimum)."""

    def backward(self, y_true_onehot: np.ndarray, cache: dict) -> dict:
        """Full backward pass via the chain rule — see the backward pass note
        above for where to start. Return {"W1":..., "b1":..., "W2":..., "b2":...}."""

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predicted class indices — argmax of forward(X)'s probs."""

    def params(self) -> dict:
        """{"W1": self.W1, "b1": self.b1, "W2": self.W2, "b2": self.b2}."""

    def gradient_check(self, X: np.ndarray, y_true_onehot: np.ndarray, eps: float = 1e-5) -> dict:
        """For each parameter array, perturb every scalar entry by +-eps,
        rerun forward + cross_entropy each time, and compare against
        backward()'s analytic gradient — same numerical_gradient pattern as
        math_concepts.md 1.2's finite-difference example, looped over every
        parameter instead of just one. Return relative error per parameter
        name. Run on a small subset (8-16 samples) — looping over every
        scalar entry is slow at full batch size."""
```

#### `train.py`

```python
def train(
    model: "TwoLayerNet",
    X_train: np.ndarray,
    y_train_onehot: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    lr: float = 0.5,
    batch_size: int = 32,
    n_epochs: int = 30,
) -> dict:
    """Mini-batch SGD. Each epoch: shuffle, iterate over batches, forward +
    backward + update each param in place (param -= lr * grad). After each
    epoch, record training loss and validation accuracy.
    Return {"train_loss": [...], "val_accuracy": [...]}, one entry per epoch."""
```

#### `visualize.py`

```python
def plot_training_curves(train_loss: list[float], val_accuracy: list[float]) -> None:
    """Two subplots sharing the epoch axis: loss on top, accuracy on bottom.
    Save to figures/training_curves.png."""
```

#### `run_experiments.py`

```python
def generate_synthetic_data(
    n_classes: int = 10, n_features: int = 30, n_samples_per_class: int = 200,
    center_scale: float = 1.0, noise_scale: float = 2.0, seed: int = 0,
) -> tuple[np.ndarray, np.ndarray]:
    """"MNIST-style" here means n_classes clusters in n_features-dim space,
    shaped like a real classification problem — not literal 28x28 images.
    For each class, sample a random center (scale=center_scale), then
    sample n_samples_per_class points around it (scale=noise_scale). Stack
    and shuffle. Return (X, y): X shape (n_classes*n_samples_per_class,
    n_features), y shape (n_classes*n_samples_per_class,) of class indices.
    These defaults are tuned to land around 70-75% val accuracy with a
    correct implementation — comfortably above the 60% bar without being
    trivial to hit."""

def main() -> None:
    """
    1. generate_synthetic_data(), split 80/20 into train/val, one-hot
       encode y_train.
    2. Build TwoLayerNet(n_features=30, n_hidden=64, n_classes=10). Check
       the loss on the full training set before any training — should
       land close to log(10) ≈ 2.303 (a random classifier's cross-entropy
       over 10 balanced classes: -log(1/10)). Explain why in a comment.
    3. Run model.gradient_check on a small batch of the training data.
       Every relative error should be under 1e-4 — if not, stop and find
       the bug in backward() before training on it.
    4. Train with train() for 30 epochs. Plot with plot_training_curves.
    """
```

**Done when:** loss at initialization is within ~0.05 of log(10) ≈ 2.303; `gradient_check`'s relative errors are all under 1e-4; validation accuracy exceeds 60% after 30 epochs; training curves (loss and accuracy) are plotted.

---

## Optional Stretch (only if you finish core projects with time to spare before Sept 27)

Do these in this priority order if you have time. Skip them entirely if you don't — none of them teach something the 4 core projects don't already cover, they just go deeper or practice the same skill in a different shape.

1. **Data Preprocessing Engine** (`StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `train_test_split` from scratch in NumPy). Reasonable to fold directly into Project 3's data-prep step instead of building standalone.
2. **Config Manager** (dot-notation config object with freezing, merging, diffing). Useful engineering pattern, lowest ML relevance of the stretch set.
3. **Mini Tensor Library** (`microtensor` — OOP wrapper around NumPy with dunder-method arithmetic). Largely superseded by Project 4 above.
4. **Mini ML Framework** (pure-Python, no NumPy, deliberately skips real backprop). Interesting for project-structure fluency but explicitly doesn't complete the learning loop (no real gradients) — lowest priority.

Ask if you want a fuller spec for any of these when you're ready to build one.

---

*Last updated: 2026-08-31*
