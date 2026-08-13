# Phase 0 — Matplotlib Concepts

Concepts, not drills — no exercises file for this one. Needed for Projects 3 & 4.

---

## The Right Mindset

Two interfaces:

- **pyplot (stateful):** `plt.plot(...)`, `plt.xlabel(...)` — implicit, acts on "current" figure/axes.
- **Object-oriented:** `fig, ax = plt.subplots()`, then `ax.plot(...)`, `ax.set_xlabel(...)` — explicit references.

Use the OO interface as default — this doc uses it throughout. pyplot-style code is common in tutorials/Stack Overflow but not used here.

---

## 1.1 — Anatomy of a Plot: Figure vs Axes

- **Figure** — the whole canvas/image. Can hold multiple plots.
- **Axes** — one plot area inside a Figure (data, x/y axis, title). Not the same as "an axis" (the x or y axis line alone).

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()          # one Figure containing one Axes
ax.plot([1, 2, 3], [1, 4, 9])     # draw on that Axes
fig.savefig("plot.png")           # save the whole Figure
```

`plt.subplots()` with no args returns one Figure, one Axes. With `nrows`/`ncols`, returns one Figure and an array of Axes — see 1.5.

---

## 1.2 — Basic Plot Types

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot — ordered sequences (loss curves, predictions over time)
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("line.png")

# Scatter plot — individual (x, y) pairs, no implied order
fig, ax = plt.subplots()
ax.scatter(x, y)
fig.savefig("scatter.png")

# Bar chart — discrete categories
fig, ax = plt.subplots()
ax.bar(["a", "b", "c"], [3, 7, 5])
fig.savefig("bar.png")

# Histogram — distribution of one variable
data = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(data, bins=30)
fig.savefig("hist.png")
```

---

## 1.3 — Labels, Titles, Legends

Non-negotiable on every plot you keep.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Sine Wave")
ax.legend()                        # only shows if plot calls used label=
fig.savefig("labeled.png")
```

OO naming pattern: `ax.set_xlabel(...)` vs pyplot's `plt.xlabel(...)`.

---

## 1.4 — Multiple Series on One Plot

Call `ax.plot()` (or `scatter`/etc.) more than once on the same `ax`; `label=` on each feeds the legend.

```python
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.legend()
fig.savefig("multi.png")
```

Pattern used in Project 3's optimizer comparison — one `ax.plot(losses, label=...)` call per run, one legend.

---

## 1.5 — Subplots and Layouts

`plt.subplots(nrows, ncols)` returns a grid; `axes` becomes an array.

```python
# 1 row, 2 columns → axes is a 1D array of length 2
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
axes[0].plot(x, np.sin(x))
axes[0].set_title("sin")
axes[1].plot(x, np.cos(x))
axes[1].set_title("cos")
fig.tight_layout()                 # prevents titles/labels overlapping
fig.savefig("subplots.png")
```

```python
# 2 rows, 2 columns → axes is a 2D array, index with [row, col]
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].hist(data, bins=20)
axes[1, 1].scatter(x[:20], y[:20])
fig.tight_layout()
fig.savefig("grid.png")
```

`figsize=(width, height)` in inches — default is small, set explicitly. Call `fig.tight_layout()` before saving whenever there's more than one Axes.

---

## 1.6 — Log Scale

For values spanning multiple orders of magnitude — e.g. loss curves.

```python
losses = 1 / np.arange(1, 101)     # stand-in for a decaying loss curve

fig, ax = plt.subplots()
ax.plot(losses)
ax.set_yscale("log")
ax.set_xlabel("epoch")
ax.set_ylabel("loss (log scale)")
fig.savefig("logscale.png")
```

`set_yscale("log")` / `set_xscale("log")`.

---

## 1.7 — Heatmaps (`imshow`)

2D grids where color encodes magnitude — used for confusion matrices in Phase 1.

```python
matrix = np.random.rand(5, 5)

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap="viridis")
fig.colorbar(im, ax=ax)            # the color-to-value key
fig.savefig("heatmap.png")
```

`imshow` returns the image object (`im`) — needed to attach the colorbar.

---

## 1.8 — Error Bars and Uncertainty Bands

```python
epochs = np.arange(1, 21)
mean_loss = 1 / epochs
std_loss = mean_loss * 0.2          # stand-in for variance across runs

# Shaded band — continuous mean +/- spread
fig, ax = plt.subplots()
ax.plot(epochs, mean_loss, label="mean loss")
ax.fill_between(
    epochs, mean_loss - std_loss, mean_loss + std_loss,
    alpha=0.3, label="±1 std",
)
ax.legend()
fig.savefig("errorband.png")

# Discrete error bars — fewer, distinct points
fig, ax = plt.subplots()
ax.errorbar(epochs, mean_loss, yerr=std_loss, fmt="-o", capsize=3)
fig.savefig("errorbar.png")
```

`alpha=` (0–1) controls transparency.

---

## 1.9 — Styling

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(
    x, np.sin(x),
    color="tab:blue",
    linestyle="--",         # "-" solid (default), "--" dashed, ":" dotted, "-." dash-dot
    linewidth=2,
    marker="o",             # point marker; omit for a clean line
    markevery=10,           # marker every 10th point
    label="sin",
)
ax.grid(True, alpha=0.3)
ax.legend()
fig.savefig("styled.png")
```

Default colormap for `imshow`/`scatter(c=...)`: `"viridis"` — perceptually uniform.

---

## 1.10 — Saving Figures

```python
fig.savefig("figure.png", dpi=150, bbox_inches="tight")
```

- `dpi=` — resolution. 150 default, 300 for written reports.
- `bbox_inches="tight"` — crops whitespace, prevents label cutoff.

Scripts have nothing that auto-displays a plot — always `fig.savefig(...)`.

---

## 1.11 — Common Pitfalls / Good Habits

```python
# 1. Close figures in a loop. Verified: 200 figures without plt.close()
#    retained ~70 MB; with plt.close(fig) after each, ~1 MB.
for i in range(5):
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x + i))
    fig.savefig(f"run_{i}.png")
    plt.close(fig)

# 2. Headless environments (servers, CI, this sandbox) need a
#    non-interactive backend, set before importing pyplot:
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 3. Set figsize explicitly — default is small.

# 4. Label every axis, every time — see 1.3.
```

---

## 1.12 — Resources

- Matplotlib official quickstart: matplotlib.org/stable/tutorials/introductory/quick_start.html
- Matplotlib cheat sheets (official, PDF): matplotlib.org/cheatsheets
- Colormap guidance (why `viridis` over rainbow-style maps): matplotlib.org/stable/users/explain/colors/colormaps.html

---

*Last updated: 2026-08-13*
