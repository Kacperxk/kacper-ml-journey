# Phase 0 Projects

Target date for all of Phase 0 (concepts + drills + projects): **September 27, 2026**.

> **Why this file exists:** the original course had three independent project lists (one each in the phase0 guide, the Python exercises doc, and the NumPy exercises doc) — 9 projects total, only 3 of which were ever wired into the actual repo structure. This file replaces all three lists with one canonical set: **4 core projects** everyone should do, and 4 **optional stretch** projects, clearly marked as skippable. Full original specs for the stretch projects still exist in your old exercise docs if you want them — this file just gives the short version and tells you where to look.

---

## Core Projects (do these, in order)

### Project 1 — CLI Weather Tool
**Focus:** Python OOP, Git, project structure, error handling, type hints
**Time:** ~1 week
**Full spec:** carry over verbatim from the original `phase0_complete.md` "Project 0.1"

Command-line app that fetches real weather data (Open-Meteo API, free, no key needed) and analyzes it. Uses a `WeatherFetcher` class, a `WeatherData` class with properties and stats methods, custom exceptions (`WeatherError`, `APIError`, `ParseError`), `argparse` CLI, logging instead of print. This is your one pure software-engineering project — OOP, an external API, error handling, and a real git history, all in one place. Nothing else in Phase 0 drills this combination.

**Done when:** CLI works end-to-end for at least 2 cities, invalid input produces a clean message (no traceback), data can be saved and reloaded, git history has 10+ meaningful commits.

---

### Project 2 — Data Pipeline
**Focus:** generators, iterators, memory-efficient data processing
**Time:** ~4–5 hours
**Full spec:** carry over verbatim from the original `python_exercises.md` "Project 2"

Chainable `Pipeline` class built on generators (`.map()`, `.filter()`, `.batch()`, `.shuffle()`, `.collect()`) that never loads a full dataset into memory. This is a distinct skill from Project 1 — it's exactly the pattern used for streaming ML training data — and doesn't overlap with anything else in Phase 0.

**Done when:** all four tests pass (basic pipeline, batch+take, memory-efficiency via `tracemalloc`, shuffle buffer).

---

### Project 3 — Linear Regression from Scratch (with visualization)
**Focus:** NumPy vectorization, gradient descent, math-to-code translation
**Time:** ~1.5 weeks
**Full spec:** merge of `phase0_complete.md` "Project 0.2" (Linear Regression from Scratch) and `numpy_exercises.md` "Project 2" (Gradient Descent Visualizer) — these were two separate projects drilling the same core skill (formula → NumPy, GD variants) and are combined here into one.

Build a `LinearRegression` class in pure NumPy, in stages:
1. Closed-form OLS solution (`np.linalg.lstsq`, not `inv` — more stable)
2. Batch gradient descent
3. Mini-batch gradient descent
4. Ridge regression (L2 regularization, don't regularize the bias term)

Then visualize: loss curves for batch vs mini-batch GD on the same plot, predictions-vs-truth scatter, weight convergence over epochs, and — folding in the GD Visualizer project — compare **vanilla GD, momentum, and Adam** on the ill-conditioned toy function `f(x,y) = x² + 5y²`, showing Adam converges faster. Test the final class on both synthetic data (recover known weights) and a real dataset (California Housing via sklearn — expect R² ~0.5–0.7).

**Done when:** gradient descent matches OLS within 0.01 on toy data, all plots exist with clear labels, code runs correctly on California Housing.

---

### Project 4 — NumPy Neural Network (capstone)
**Focus:** full forward/backward pass, gradient checking, mini-batch training
**Time:** ~6–10 hours
**Full spec:** carry over verbatim from the original `numpy_exercises.md` "Project 3"

A `TwoLayerNet` class (`Linear → ReLU → Linear → Softmax`, cross-entropy loss) implemented entirely in NumPy, including manual backward pass via the chain rule. Trained with mini-batch SGD on synthetic MNIST-style data. Must pass a numerical gradient check (`gradient_check` function, relative error < 1e-4) before you trust the training results.

This is the Phase 0 capstone and directly sets up Phase 2's PyTorch/backprop work — it fully replaces the need for the two "stretch" tensor-wrapper projects below, which cover the same ground at lower depth.

**Done when:** loss ≈ log(10) ≈ 2.3 at initialization, gradient check passes, validation accuracy exceeds 60% after 30 epochs, training curves plotted.

---

## Optional Stretch (only if you finish core projects with time to spare before Sept 27)

Do these in this priority order if you have time. Skip them entirely if you don't — none of them teach something the 4 core projects don't already cover, they just go deeper or practice the same skill in a different shape.

1. **Data Preprocessing Engine** (`StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `train_test_split` from scratch in NumPy) — full spec in the original `numpy_exercises.md` "Project 1". Reasonable to fold directly into Project 3's data-prep step instead of building standalone.
2. **Config Manager** (dot-notation config object with freezing, merging, diffing) — full spec in the original `python_exercises.md` "Project 1". Useful engineering pattern, lowest ML relevance of the stretch set.
3. **Mini Tensor Library** (`microtensor` — OOP wrapper around NumPy with dunder-method arithmetic) — full spec in the original `phase0_complete.md` "Project 0.3". Largely superseded by Project 4 above.
4. **Mini ML Framework** (pure-Python, no NumPy, deliberately skips real backprop) — full spec in the original `python_exercises.md` "Project 3". Interesting for project-structure fluency but explicitly doesn't complete the learning loop (no real gradients) — lowest priority.

---

*Last updated: 2026-08-04*
