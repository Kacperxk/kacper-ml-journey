# pandas & SQL — Concepts (Module 1A)

Reading guide + notes for `pandas_exercises.md`. The reading is the teaching material; notes below cover what the books skip, what changed in pandas 3, and links back to Phase 0. Drills assume the section's reading is done.

**Main book:** *Python for Data Analysis*, 3rd ed. (McKinney), free at wesmckinney.com/book — written for pandas 2.0. Where pandas 3 behaves differently, the notes below say so.

**Setup check** (first cell of every notebook in this module):

```python
import numpy as np
import pandas as pd

assert pd.__version__.startswith("3."), pd.__version__
```

---

## Section 1 — Series & DataFrame fundamentals

**Read:** McKinney 5.1; 5.2 "Reindexing", "Dropping Entries from an Axis", "Arithmetic and Data Alignment", "Sorting and Ranking"; 5.3; ch. 6 on text files (`read_csv`) and binary formats (Parquet).

- **Series** = a 1-D NumPy-like array + an **index** of labels. **DataFrame** = a dict of Series sharing one row index. Each column has exactly one dtype — a DataFrame is a table of typed columns, not a 2-D array.
- **Index alignment.** Arithmetic between Series matches *labels*, not positions — the biggest difference from NumPy. Labels present in only one side give `NaN`. Integer data becomes `float64` as soon as a `NaN` appears, because `NaN` is a float. `s1.add(s2, fill_value=0)` treats a missing side as 0 instead.
- `df["col"]` returns a Series; `df[["col"]]` returns a one-column DataFrame.
- First look at any table: `shape`, `dtypes`, `info()`, `head()`, `describe()`.
- **pandas 3:** text columns get the dedicated `str` dtype, not `object` (McKinney shows `object`).
- **CSV vs Parquet.** CSV is plain text: every dtype is re-guessed on read, and dates come back as strings unless you parse them. Parquet stores the schema: dtypes survive a round trip. Use Parquet for your own intermediate files.

## Section 2 — Indexing, selection & Copy-on-Write

**Read:** McKinney 5.2 "Indexing, Selection, and Filtering"; pandas user guide "Copy-on-Write (CoW)".

- `.loc` selects by **label** (slice end *included*); `.iloc` by **position** (slice end *excluded*, like Python). `[]` selects columns, or rows by a boolean mask.
- Boolean masks combine with `&`, `|`, `~` — each condition in parentheses, since `&` binds tighter than `>`. Also `.isin()`, `.between()`.
- Setting values: one step, `df.loc[mask, "col"] = value`.
- **Copy-on-Write** (the only mode in pandas 3): every selection behaves like a new, independent object. Modifying a filtered subset never changes the original, and vice versa. Internally the data is shared until one side is written to, so selections stay cheap.
- **Chained assignment never works:** `df["col"][mask] = value` — the first `[]` produces a (lazy) copy, and the assignment lands on that copy. pandas warns with `ChainedAssignmentError`. Use `.loc`.
- **Contrast with NumPy** (`docs/phase0/numpy_concepts.md`): a NumPy basic slice is a *view*, so writing to it changes the original. pandas 3 chose the opposite default. `.to_numpy()` can return a read-only view of a column — writing to it raises `ValueError`; use `.to_numpy(copy=True)` if you need a writable array.
- Older tutorials (and some of McKinney) mention `SettingWithCopyWarning`. It no longer exists in pandas 3.

## Section 3 — Cleaning: missing data, dtypes, strings

**Read:** McKinney 7.1–7.5; pandas user guide "Working with text data".

- Missing values can appear as `NaN`, `None`, `pd.NA`, or `NaT` (dates). `isna()` catches all of them.
- Aggregations skip missing values by default (`skipna=True`): `mean()` of `[1, NaN, 3]` is `2.0`. `count()` counts non-missing values.
- An integer column with one missing value becomes `float64`. The nullable `"Int64"` dtype keeps integers and uses `pd.NA`.
- **Converting:** `astype()` for data you know is clean; `pd.to_numeric(s, errors="coerce")` turns anything unparseable into `NaN` — always count how many values that silently dropped.
- **Strings:** the `.str` accessor applies string methods to a whole column and skips missing values. In pandas 3, missing strings are `NaN`.
- **Duplicates:** `duplicated()` / `drop_duplicates(subset=..., keep=...)`. Normalise text (strip, lowercase) *before* deduplicating — `" Anna"` and `"anna"` are different strings.
- **Categorical dtype:** a fixed set of allowed values. An *ordered* categorical sorts by the declared order (`S < M < L`), not alphabetically.

## Section 4 — Transforming & groupby

**Read:** McKinney 5.2 "Function Application and Mapping"; 7.2 (`map`, `replace`, `cut`/`qcut`); 10.1–10.4.

- Prefer vectorized operations. `Series.map(dict)` for lookups. Row-wise `apply(axis=1)` is a Python loop in disguise — slow, and rarely needed.
- `assign()` adds columns inside a method chain.
- **Split–apply–combine** has three result shapes:
  - **aggregate** — one row per group (`sum`, `mean`, named aggregation);
  - **transform** — same length as the input, each row gets its group's value back (e.g. share of group total);
  - **filter** — keeps or drops whole groups.
- **Named aggregation:** `df.groupby("k").agg(total=("amount", "sum"), n=("amount", "count"))`.
- `size()` counts rows including missing; `count()` counts non-missing values.
- Group keys become the index of the result; `reset_index()` or `as_index=False` turns them back into columns.
- **pandas 3:** grouping by a categorical column shows only categories that actually occur (`observed=True` is the default), and `groupby().apply()` no longer passes the grouping columns to your function. Prefer `agg`/`transform`.

## Section 5 — Combining: concat & merge

**Read:** McKinney 8.2.

- `pd.concat` stacks tables (rows by default). `ignore_index=True` builds a fresh 0..n−1 index. Columns missing from one table become `NaN`.
- `merge` is a SQL join: `how="inner" | "left" | "right" | "outer"`; `on=`, or `left_on=`/`right_on=`; `suffixes=` for clashing column names.
- **Row counts follow key cardinality.** One-to-many repeats the "one" side's rows. Many-to-many produces every combination — a silent row explosion.
- `validate="one_to_one"` / `"many_to_one"` checks key uniqueness and raises `MergeError` if it doesn't hold.
- `indicator=True` adds a `_merge` column (`both` / `left_only` / `right_only`) — the standard way to find rows with no match (an anti-join).
- Check the row count before and after every merge.

## Section 6 — Reshaping & time

**Read:** McKinney 8.1 (MultiIndex basics), 8.3, 10.5, 11.1–11.3, 11.6.

- **Long** format has one row per observation; **wide** spreads one variable across columns. `melt` goes wide → long; `pivot` / `pivot_table` go long → wide.
- `pivot` requires each (index, column) pair to be unique and raises `ValueError` otherwise; `pivot_table` aggregates duplicates (`aggfunc=`, `fill_value=`, `margins=`).
- `stack` / `unstack` move a level between the row index and the columns.
- **Datetimes:** `pd.to_datetime`, the `.dt` accessor (`year`, `month`, `day_name()`), `pd.Timedelta`, `pd.date_range`.
- `resample` (calendar-period aggregation), `rolling` windows, and `shift`/`diff` work on a `DatetimeIndex`. `resample("W")` labels each week by its **ending Sunday**.
- **pandas 3:** datetime resolution is inferred, not always nanoseconds — check dates with `pd.api.types.is_datetime64_any_dtype`, not by comparing to `"datetime64[ns]"`. Month-end frequency is `"ME"` (`"M"` is gone).

## Section 7 — EDA & visualization

**Read:** McKinney 5.3, 9.2; seaborn user guide, "An introduction to seaborn" and "Overview of seaborn plotting functions"; Géron ch. 2, the data exploration part.

- **EDA checklist:** shape and dtypes → missing values → each column's distribution → relationships between columns → the target → quality flags (duplicates, impossible values, outliers).
- `value_counts(normalize=True)` for shares; `pd.crosstab(a, b, normalize="index")` for row-wise shares.
- **Correlation** (Pearson) measures *linear* association only, from −1 to 1. Sensitive to outliers; blind to non-linear relationships; says nothing about causation. `method="spearman"` measures monotonic association.
- seaborn **axes-level** functions (`histplot`, `boxplot`, `scatterplot`, `heatmap`, ...) take `ax=` and return the Axes — the same Figure/Axes style as `docs/phase0/matplotlib_concepts.md`. **Figure-level** functions (`displot`, `relplot`, `catplot`, `pairplot`) create their own figure.
- **IQR outlier rule:** values below Q1 − 1.5·IQR or above Q3 + 1.5·IQR, where IQR = Q3 − Q1. A flag to investigate, not a reason to delete.

## Section 8 — SQL with DuckDB

**Read:** DuckDB documentation — the SQL introduction, the Python API overview (including querying pandas DataFrames), and window functions.

- Most real data lives in SQL databases, and SQL is a standard interview skill. DuckDB is an analytical database that runs inside your Python process — no server. `duckdb.sql("SELECT ... FROM df")` finds the DataFrame named `df` in your Python code; `.df()` returns the result as a pandas DataFrame.
- **Logical order of a query:** `FROM`/`JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`. This is why `WHERE` can't use an aggregate (groups don't exist yet) and `HAVING` can.

| pandas | SQL |
|---|---|
| `df[df.x > 5]` | `WHERE x > 5` |
| `df.groupby("k").agg(...)` | `GROUP BY k` |
| filter on an aggregate | `HAVING` |
| `df.merge(o, how="left")` | `LEFT JOIN` |
| `fillna(0)` | `COALESCE(x, 0)` |
| `groupby().transform` / `cumsum` / `rank` | window functions: `... OVER (PARTITION BY ... ORDER BY ...)` |
| `size()` vs `count()` | `COUNT(*)` vs `COUNT(col)` |

- **Window functions** compute a value for every row from a group of related rows *without collapsing them* — running totals, ranks, previous value (`LAG`).
- `WITH name AS (...)` (a CTE) names an intermediate result, like assigning a variable.
- **NULL:** `x = NULL` is never true — use `IS NULL`. Aggregates skip NULLs, like pandas skips `NaN`. When sorting, `ORDER BY x DESC NULLS LAST` keeps missing values at the end.
- DuckDB queries files directly by path: `SELECT ... FROM 'orders.parquet'` — no loading into pandas first.

---

*Last updated: 2026-09-29*
