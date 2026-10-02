# Phase 1 — Mastery Log

Depth of load-bearing concepts, backed by evidence. Separate from `phase1/README.md`, which tracks completion. Scale and definitions: `docs/mastery/phase0.md`.

## 1A — pandas & SQL

- **Index alignment (label vs. positional arithmetic, NaN → float upcast)** — *Understood*, 2026-10-01. Ex 1.1: predicted index, values and dtype of both `s1 + s2` and `s1 + s2.to_numpy()` correctly. First explanation was wrong: "float because we are adding two Series" (`s1 + s1` stays `int64`). After two rounds of prompting, restated the full chain: labels only on one side → `NaN` → `int64` can't hold it → `float64`. Also explained, on the first attempt, why `add(..., fill_value=0)` stays `float64` (NaN is created during realignment, before the fill, and isn't cast back).
- **`df["col"]` vs `df[["col"]]` (key type decides Series vs DataFrame)** — *Understood*, 2026-10-02. Ex 1.2: predictions right. First explanation was wrong ("inner brackets make a 2-D array"). After correction, applied the rule correctly to `books[["title", "price"]]`. Why `books["title", "price"]` fails (a tuple is looked up as one label → `KeyError`) was only half-explained and then given by Claude.
- **One dtype per column vs. one per array (`to_numpy()` upcasting)** — *Understood*, 2026-10-02. Ex 1.3: dtypes predicted correctly. Used `include=["int", "float"]`, which misses unsigned ints; `"number"` recommended. Predicted `to_numpy()` → `object` correctly, but the reason started vague ("can't find better dtype") until Claude filled in why no numeric dtype fits text. Then applied it correctly to a new case: `[["year", "price"]].to_numpy()` → `float64`, with the reason.

---

*Last updated: 2026-10-01*
