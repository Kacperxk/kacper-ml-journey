# pandas & SQL Exercises — Module 1A
## 41 exercises (several multi-part) across 8 sections

---

> **How to use this document:** one notebook per section, `phase1/pandas/section<N>_<topic>.ipynb`. Do the section's reading in `pandas_concepts.md` first. Every section starts with a **setup cell** — paste it in as given; its functions return a fresh copy of the data each call, so exercises don't affect each other.

> **The rules, same as Phase 0:** for every *Predict* item, write your prediction as a comment **before** running. Where you see `...`, write the code. Every task ends in `assert`s — they must pass as given; don't edit them.

---

# SECTION 1 — Series & DataFrame fundamentals
*Skills: index alignment, building frames, dtypes, sorting, CSV vs Parquet*

**Setup:**

```python
import tempfile
import pathlib
import numpy as np
import pandas as pd

assert pd.__version__.startswith("3."), pd.__version__

def make_books() -> pd.DataFrame:
    return pd.DataFrame({
        "title": ["Dune", "Neuromancer", "Foundation", "Hyperion",
                  "The Left Hand of Darkness", "Snow Crash"],
        "author": ["Herbert", "Gibson", "Asimov", "Simmons", "Le Guin", "Stephenson"],
        "year": [1965, 1984, 1951, 1989, 1969, 1992],
        "pages": [412, 271, 255, 482, 304, 480],
        "price": [18.99, 14.50, 12.00, 17.25, 15.75, 16.40],
    })
```

---

**Exercise 1.1** — Index alignment.

A) Predict the index, values, and dtype of `r` and `r_np`:

```python
s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])

r = s1 + s2                  # predict: index? values? dtype?
r_np = s1 + s2.to_numpy()    # predict: index? values? dtype?
```

In a comment: why is `r` float while `r_np` is int, and why do the two give different numbers for the same inputs?

B) Add `s1` and `s2` so that a label missing on one side counts as 0:

```python
filled = ...

assert filled.to_dict() == {"a": 1.0, "b": 12.0, "c": 23.0, "d": 30.0}
assert filled.dtype == "float64"
```

---

**Exercise 1.2** — Building on a DataFrame.

```python
books = make_books()

# A) Add "price_per_100_pages": price per 100 pages, rounded to 2 decimals.
...

assert books["price_per_100_pages"].tolist() == [4.61, 5.35, 4.71, 3.58, 5.18, 3.42]

# B) Make a new frame with "title" as the index.
by_title = ...

assert by_title.loc["Dune", "year"] == 1965
assert by_title.shape == (6, 5)
```

C) Predict: `type(books["price"])`, `type(books[["price"]])`, and `books.shape` after part A.

---

**Exercise 1.3** — dtypes.

A) Predict every entry of `make_books().dtypes`. What dtype do the text columns get in pandas 3 — and what does McKinney's book show instead?

B) Select columns by dtype:

```python
books = make_books()
numeric = ...   # only the numeric columns
text = ...      # only the text columns

assert list(numeric.columns) == ["year", "pages", "price"]
assert list(text.columns) == ["title", "author"]
assert books["title"].dtype == "str"
```

---

**Exercise 1.4** — Sorting and ranking.

```python
books = make_books()

newest_first = ...   # all books, newest year first
top2 = ...           # the 2 most expensive books (one method call)

assert newest_first["title"].tolist() == ["Snow Crash", "Hyperion", "Neuromancer",
                                          "The Left Hand of Darkness", "Dune", "Foundation"]
assert top2["title"].tolist() == ["Dune", "Hyperion"]

# Rank by pages: the longest book gets rank 1.0.
books["pages_rank"] = ...

assert books.set_index("title")["pages_rank"].to_dict() == {
    "Dune": 3.0, "Neuromancer": 5.0, "Foundation": 6.0, "Hyperion": 1.0,
    "The Left Hand of Darkness": 4.0, "Snow Crash": 2.0}
```

Predict: which statistics does `books["price"].describe()` return (the index labels)? Then:

```python
desc = books["price"].describe()
assert desc["max"] == 18.99 and desc["count"] == 6
```

---

**Exercise 1.5** — CSV vs Parquet.

```python
books = make_books()
books["published"] = pd.to_datetime(books["year"].astype(str) + "-01-01")
books["format"] = pd.Categorical(["hardcover", "paperback", "paperback",
                                  "hardcover", "paperback", "ebook"])

with tempfile.TemporaryDirectory() as tmp:
    csv_path = pathlib.Path(tmp) / "books.csv"
    parquet_path = pathlib.Path(tmp) / "books.parquet"

    # A) Write books to both files (no index column in the CSV), then read both back.
    ...
    from_csv = ...
    from_parquet = ...

    # Predict before printing: the dtype of "published" and "format" in each.
    print(from_csv.dtypes, from_parquet.dtypes, sep="\n\n")

    assert pd.api.types.is_string_dtype(from_csv["published"])
    assert pd.api.types.is_string_dtype(from_csv["format"])
    assert pd.api.types.is_datetime64_any_dtype(from_parquet["published"])
    assert isinstance(from_parquet["format"].dtype, pd.CategoricalDtype)

    # B) Read the CSV again so that "published" comes back as a datetime.
    fixed = ...

    assert pd.api.types.is_datetime64_any_dtype(fixed["published"])
```

In a comment: which of the two formats would you use for an intermediate file in a project, and why?

---

# SECTION 2 — Indexing, selection & Copy-on-Write
*Skills: `.loc` vs `.iloc`, boolean masks, setting values safely, Copy-on-Write*

**Setup:** same imports and `make_books()` as Section 1.

---

**Exercise 2.1** — `.loc` vs `.iloc` when the index isn't 0..n−1.

```python
b = make_books()
b.index = [10, 20, 30, 40, 50, 60]

print(b.loc[20:40, "title"].tolist())   # predict
print(b.iloc[1:3]["title"].tolist())    # predict
print(type(b.loc[20]).__name__)         # predict
print(b.iloc[-1]["title"])              # predict
```

Then:

```python
picked = ...       # rows labelled 30 and 50, columns "title" and "price"
first_two = ...    # first 2 rows and first 2 columns, by position

assert picked.shape == (2, 2)
assert picked["title"].tolist() == ["Foundation", "The Left Hand of Darkness"]
assert first_two.to_dict() == {"title": {10: "Dune", 20: "Neuromancer"},
                               "author": {10: "Herbert", 20: "Gibson"}}
```

---

**Exercise 2.2** — Boolean filtering.

```python
books = make_books()

old_and_pricey = ...   # published before 1980 AND price above 15
cyber = ...            # written by Gibson or Stephenson (use .isin)
mid = ...              # between 300 and 450 pages, inclusive (use .between)
not_asimov = ...       # every book not by Asimov (use ~)

assert old_and_pricey["title"].tolist() == ["Dune", "The Left Hand of Darkness"]
assert cyber["title"].tolist() == ["Neuromancer", "Snow Crash"]
assert mid["title"].tolist() == ["Dune", "The Left Hand of Darkness"]
assert len(not_asimov) == 5
```

Predict: what happens when you run the line below, and why? Fix it in a comment.

```python
books[books["year"] < 1980 & books["price"] > 15]
```

---

**Exercise 2.3** — Copy-on-Write.

A) Predict whether `books` changes after each block, then run it:

```python
books = make_books()
cheap = books[books["price"] < 15]
cheap.loc[:, "price"] = 0.0
print(books["price"].tolist(), cheap["price"].tolist())   # predict both
```

```python
books = make_books()
books["price"][books["year"] < 1960] = 99.0   # predict: does books change? what does pandas print?
print(books["price"].tolist())
```

B) Give every book published before 1970 a 10% discount, correctly, in one statement:

```python
books = make_books()
...

assert np.allclose(books["price"], [17.091, 14.50, 10.80, 17.25, 14.175, 16.40])
```

---

**Exercise 2.4** — pandas vs NumPy: views.

Predict all three printed results:

```python
arr = np.array([1.0, 2.0, 3.0])
view = arr[:2]
view[0] = 100.0
print(arr)                  # predict (Phase 0 rule)

s = pd.Series([1.0, 2.0, 3.0])
sub = s[:2]
sub.iloc[0] = 100.0
print(s.tolist())           # predict

vals = s.to_numpy()
vals[0] = 100.0             # predict: what happens?
```

Then get a NumPy array you're allowed to modify, double it, and show `s` is untouched:

```python
doubled = ...
...

assert doubled.tolist() == [2.0, 4.0, 6.0]
assert s.tolist() == [1.0, 2.0, 3.0]
```

In a comment: why would pandas choose the opposite default from NumPy?

---

# SECTION 3 — Cleaning: missing data, dtypes, strings
*Skills: finding missing values, numeric conversion, text normalisation, deduplication, categoricals*

**Setup:**

```python
import numpy as np
import pandas as pd

def make_raw() -> pd.DataFrame:
    return pd.DataFrame({
        "name": ["  Anna Kowalska", "anna kowalska", "Piotr Nowak ", "EWA ZIELINSKA",
                 "Jan Wisniewski", None],
        "email": ["ANNA@MAIL.COM", "anna@mail.com ", "piotr@mail.com", "ewa@mail.com",
                  None, "ghost@mail.com"],
        "age": ["34", "34", "N/A", "29", "forty", "51"],
        "city": ["Warszawa, PL", "Warszawa, PL", "Krakow, PL", "Berlin, DE",
                 "Gdansk, PL", "Oslo, NO"],
        "size": ["M", "M", "L", "S", "XL", "M"],
    })
```

---

**Exercise 3.1** — What counts as missing? Predict every output:

```python
raw = make_raw()
print(raw.isna().sum())     # predict each column — careful with "age"
print(raw.dtypes)           # predict

x = pd.Series([1, None, 3])
print(x.dtype)              # predict
print(x.mean(), x.sum())    # predict
print(x.count(), x.size)    # predict

xi = x.astype("Int64")
print(xi.dtype, xi.tolist())   # predict
```

---

**Exercise 3.2** — Numbers stored as text.

```python
raw = make_raw()
age = ...   # "age" as numbers; anything unparseable becomes NaN

assert age.isna().sum() == 2
assert age.mean() == 37.0

# Which original strings failed to parse? Select them from raw["age"].
failed = ...

assert failed.tolist() == ["N/A", "forty"]
```

---

**Exercise 3.3** — Normalise, then deduplicate.

```python
raw = make_raw()

# Predict: how many duplicate emails does raw have right now?
print(raw.duplicated(subset="email").sum())

clean = raw.copy()
# A) "name": strip whitespace, then Title Case. "email": strip whitespace, then lowercase.
...
# B) Drop rows with a duplicate email, keeping the first.
...

assert len(clean) == 5
assert clean["name"].tolist()[:4] == ["Anna Kowalska", "Piotr Nowak", "Ewa Zielinska", "Jan Wisniewski"]
assert clean["name"].isna().sum() == 1
assert clean["email"].isna().sum() == 1
```

In a comment: why must normalising come before deduplicating?

---

**Exercise 3.4** — Splitting a text column.

```python
raw = make_raw()
parts = ...   # "city" split on ", " into two columns
parts.columns = ["city_name", "country"]

assert parts["country"].value_counts().to_dict() == {"PL": 4, "DE": 1, "NO": 1}
assert parts["city_name"].tolist() == ["Warszawa", "Warszawa", "Krakow", "Berlin", "Gdansk", "Oslo"]
```

---

**Exercise 3.5** — Dropping vs filling.

```python
raw = make_raw()
with_email = ...   # drop only rows where "email" is missing
named = ...        # fill missing "name" with "unknown"; leave other columns alone

assert len(with_email) == 5
assert named["name"].iloc[-1] == "unknown"
assert named["email"].isna().sum() == 1
```

---

**Exercise 3.6** — Ordered categoricals.

```python
raw = make_raw()
print(raw["size"].sort_values().tolist())   # predict: string sort order

raw["size"] = ...   # ordered categorical: S < M < L < XL

assert raw["size"].sort_values().tolist() == ["S", "M", "M", "M", "L", "XL"]
assert (raw["size"] > "M").sum() == 2
```

---

# SECTION 4 — Transforming & groupby
*Skills: named aggregation, size vs count, transform, map, binning, filter*

**Setup:**

```python
import numpy as np
import pandas as pd

def make_orders() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "customer": ["anna", "piotr", "anna", "ewa", "piotr", "anna", "jan", "ewa"],
        "category": ["books", "games", "books", "music", "books", "games", "music", "books"],
        "amount": [40.0, 120.0, 25.0, 15.0, 60.0, 80.0, 30.0, None],
        "qty": [2, 1, 1, 3, 2, 1, 1, 2],
    })
```

---

**Exercise 4.1** — Named aggregation.

```python
orders = make_orders()
summary = ...   # per category: total (sum of amount), avg (mean of amount), n_orders (count of order_id)

assert summary.loc["books", "total"] == 125.0
assert np.isclose(summary.loc["books", "avg"], 125 / 3)
assert summary["n_orders"].to_dict() == {"books": 4, "games": 2, "music": 2}
assert summary.index.tolist() == ["books", "games", "music"]

flat = ...      # summary with "category" back as a regular column

assert flat.columns.tolist() == ["category", "total", "avg", "n_orders"]
```

In a comment: why is books' `avg` 125/3 and not 125/4?

---

**Exercise 4.2** — `size` vs `count`. Predict each dict:

```python
orders = make_orders()
print(orders.groupby("category")["amount"].size().to_dict())    # predict
print(orders.groupby("category")["amount"].count().to_dict())   # predict
print(orders.groupby("customer").size().to_dict())              # predict (also: key order?)
```

---

**Exercise 4.3** — Transform: a group value on every row.

```python
orders = make_orders()

# A) Each order's share of its customer's total amount.
orders["share"] = ...

assert np.isclose(orders.loc[orders["customer"] == "anna", "share"].sum(), 1.0)
assert orders.loc[3, "share"] == 1.0
assert np.isnan(orders.loc[7, "share"])

# B) Each order's amount minus its category's mean amount.
orders["amount_vs_cat_mean"] = ...

assert np.isclose(orders.loc[1, "amount_vs_cat_mean"], 20.0)
```

In a comment: why does `agg` not work here, and what's the difference in output shape?

---

**Exercise 4.4** — `map`, binning, and `np.where`.

```python
orders = make_orders()
dept = {"books": "media", "music": "media", "games": "entertainment"}

orders["dept"] = ...   # look up each category in dept
assert orders["dept"].value_counts().to_dict() == {"media": 6, "entertainment": 2}

# Bands: (0, 30] small, (30, 100] medium, above 100 large.
orders["band"] = ...
counts = orders["band"].value_counts()
assert counts.to_dict() == {"small": 3, "medium": 3, "large": 1}
assert orders.loc[6, "band"] == "small"

# "bulk" where qty >= 2, otherwise "single" — no loop, no apply.
orders["bulk"] = ...
assert orders["bulk"].tolist().count("bulk") == 4
```

Predict: which band does the order with a missing amount get, and why isn't it counted?

---

**Exercise 4.5** — Filtering whole groups.

```python
orders = make_orders()
regulars = ...      # all orders of customers with at least 2 orders
big_spenders = ...  # all orders of customers whose total amount is above 100

assert len(regulars) == 7
assert sorted(regulars["customer"].unique()) == ["anna", "ewa", "piotr"]
assert sorted(big_spenders["customer"].unique()) == ["anna", "piotr"]
```

---

# SECTION 5 — Combining: concat & merge
*Skills: join types, row counts, `validate`, anti-joins, concat*

**Setup:** `make_orders()` from Section 4, plus:

```python
def make_customers() -> pd.DataFrame:
    return pd.DataFrame({
        "customer": ["anna", "piotr", "ewa", "jan", "ola"],
        "city": ["Warszawa", "Krakow", "Berlin", "Gdansk", "Oslo"],
    })

def make_categories() -> pd.DataFrame:
    return pd.DataFrame({   # vat: sales tax rate, e.g. 0.23 = 23%
        "category": ["books", "games", "music", "film"],
        "vat": [0.05, 0.23, 0.23, 0.08],
    })
```

---

**Exercise 5.1** — Predict the number of rows, then check:

```python
orders, customers, categories = make_orders(), make_customers(), make_categories()

print(len(orders.merge(customers, on="customer", how="inner")))       # predict
print(len(customers.merge(orders, on="customer", how="left")))        # predict
print(len(orders.merge(categories, on="category", how="outer")))      # predict
print(len(orders.merge(categories, on="category", how="inner")))      # predict
```

For each, explain the number in one comment line.

---

**Exercise 5.2** — Enriching orders.

```python
orders, categories = make_orders(), make_categories()

with_vat = ...   # every order with its category's vat; must check each category appears once
with_vat["gross"] = ...   # amount including vat

assert len(with_vat) == len(orders)
assert np.isclose(with_vat["gross"].sum(), 432.6)
assert with_vat.columns.tolist() == ["order_id", "customer", "category", "amount", "qty", "vat", "gross"]
```

---

**Exercise 5.3** — Anti-join: customers with no orders.

```python
orders, customers = make_orders(), make_customers()
m = ...   # customers merged with the distinct customers in orders, with an indicator column
no_orders = ...

assert no_orders == ["ola"]
```

Predict: `m["_merge"].value_counts()` — including the category that has 0.

---

**Exercise 5.4** — The many-to-many trap.

```python
orders = make_orders()
categories_dup = pd.concat(
    [make_categories(), pd.DataFrame({"category": ["books"], "vat": [0.08]})],
    ignore_index=True,
)

print(len(orders.merge(categories_dup, on="category", how="left")))   # predict
orders.merge(categories_dup, on="category", how="left", validate="many_to_one")   # predict
```

Fix the lookup table (keep the first vat for each category), then merge safely:

```python
fixed_cats = ...
fixed = ...

assert len(fixed) == 8
assert fixed.loc[fixed["category"] == "books", "vat"].unique().tolist() == [0.05]
```

---

**Exercise 5.5** — Stacking tables.

```python
orders = make_orders()
jan = orders.iloc[:4]
feb = orders.iloc[4:].reset_index(drop=True).assign(promo=[True, False, False, True])

no_ignore = pd.concat([jan, feb])
print(no_ignore.index.tolist())      # predict
print(len(no_ignore.loc[0]))         # predict — and why is this a problem?

both = ...   # jan and feb stacked, with a fresh 0..7 index

assert both.shape == (8, 6)
assert both["promo"].isna().sum() == 4
assert both.index.tolist() == list(range(8))
```

---

# SECTION 6 — Reshaping & time
*Skills: datetimes, pivot vs pivot_table, melt, resample, rolling, stack/unstack*

**Setup:**

```python
import numpy as np
import pandas as pd

def make_sales() -> pd.DataFrame:
    return pd.DataFrame({
        "date": ["2026-03-02", "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-05",
                 "2026-03-09", "2026-03-10", "2026-03-12", "2026-03-15"],
        "category": ["books", "games", "books", "books", "music",
                     "books", "games", "books", "music"],
        "amount": [20.0, 50.0, 35.0, 5.0, 10.0, 15.0, 60.0, 25.0, 30.0],
    })
```

---

**Exercise 6.1** — Working with dates.

```python
sales = make_sales()
print(sales["date"].dtype)   # predict

sales["date"] = ...          # convert to datetime
sales["weekday"] = ...       # weekday name, e.g. "Monday"

assert pd.api.types.is_datetime64_any_dtype(sales["date"])
assert sales["weekday"].value_counts()["Monday"] == 3

span = ...   # time between the first and last sale
assert span == pd.Timedelta(days=13)
```

---

**Exercise 6.2** — `pivot` vs `pivot_table`.

```python
sales = make_sales()
sales.pivot(index="date", columns="category", values="amount")   # predict: what happens, and why?
```

```python
wide = ...   # one row per date, one column per category, summed amounts, 0 where no sale

assert wide.shape == (7, 3)
assert wide.loc["2026-03-03", "books"] == 40.0
assert wide.columns.tolist() == ["books", "games", "music"]

totals = ...   # total amount per category, plus an "All" row (margins)

assert totals.loc["All", "amount"] == 250.0
```

---

**Exercise 6.3** — Wide to long and back.

```python
scores = pd.DataFrame({"student": ["ala", "bartek", "celina"],
                       "math": [5, 3, 4], "physics": [4, 5, 3]})

long = ...   # columns: student, subject, grade
assert long.shape == (6, 3)
assert long.columns.tolist() == ["student", "subject", "grade"]
assert long.loc[(long["student"] == "bartek") & (long["subject"] == "physics"), "grade"].item() == 5

back = ...   # long back to one row per student
assert back.loc["celina", "math"] == 4
```

---

**Exercise 6.4** — Resampling, rolling windows, shifts.

```python
sales = make_sales()
sales["date"] = pd.to_datetime(sales["date"])
ts = sales.set_index("date")["amount"]

weekly = ...   # total amount per calendar week
print(weekly)  # predict the two labels before printing (see pandas_concepts.md Section 6)

assert weekly.tolist() == [120.0, 130.0]
assert [str(d.date()) for d in weekly.index] == ["2026-03-08", "2026-03-15"]
assert weekly.diff().iloc[-1] == 10.0

daily = ...    # total per calendar day, including days with no sales
assert len(daily) == 14
assert daily["2026-03-04"] == 0.0

roll = ...     # 3-day rolling mean of daily
assert np.isnan(roll.iloc[0])
assert np.isclose(roll.iloc[2], (70 + 40 + 0) / 3)

assert daily.shift(1).iloc[1] == 70.0
```

Predict: why is `roll.iloc[0]` NaN?

---

**Exercise 6.5** — MultiIndex, stack and unstack.

```python
sales = make_sales()
by_two = sales.groupby(["category", "date"])["amount"].sum()
print(by_two.index.nlevels, len(by_two))   # predict both

table = ...   # move "category" into the columns, 0 where missing

assert table.shape == (7, 3)
assert table.stack().sum() == 250.0
```

---

# SECTION 7 — EDA & visualization
*Skills: profiling a table, shares and crosstabs, correlation, seaborn on Axes, outliers*

**Setup:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

**Exercise 7.1** — A reusable profile.

Write `profile(df)`: one row per column of `df`, with columns `dtype` (as a string), `n_missing`, `n_unique`.

```python
def profile(df: pd.DataFrame) -> pd.DataFrame:
    ...

small = pd.DataFrame({"a": [1, 2, 2, None], "b": ["x", "y", None, None], "c": [True, True, True, True]})
p = profile(small)

assert p.index.tolist() == ["a", "b", "c"]
assert p["n_missing"].tolist() == [1, 2, 0]
assert p["n_unique"].tolist() == [2, 2, 1]
assert p.loc["a", "dtype"] == "float64"
```

Predict: why is column `a` float64, and why doesn't `n_unique` count the missing value?

---

**Exercise 7.2** — Shares and crosstabs.

```python
survey = pd.DataFrame({   # churned: the customer cancelled their subscription
    "plan": ["free", "free", "pro", "free", "pro", "team", "free", "pro"],
    "churned": [True, False, False, True, False, False, False, True],
})

shares = ...   # share of rows per plan
assert shares.to_dict() == {"free": 0.5, "pro": 0.375, "team": 0.125}

ct = ...       # plan × churned, each row summing to 1
assert ct.loc["free", True] == 0.5
assert np.isclose(ct.loc["pro", True], 1 / 3)
assert np.allclose(ct.sum(axis=1), 1.0)

churn_rate = ...   # churn rate per plan, using groupby and the fact that True == 1
assert np.allclose(churn_rate, ct[True])
```

---

**Exercise 7.3** — Correlation and its limits.

```python
rng = np.random.default_rng(0)
n = 200
x = rng.normal(50, 10, n)
data = pd.DataFrame({"x": x, "y": 2 * x + rng.normal(0, 5, n), "z": rng.normal(0, 1, n)})
```

Predict: roughly how large are corr(x, y) and corr(x, z)? Then:

```python
corr = ...   # Pearson correlation matrix of data

assert corr.loc["x", "y"] > 0.9
assert abs(corr.loc["x", "z"]) < 0.3
assert np.allclose(np.diag(corr), 1.0)
```

Now a perfect but non-linear relationship:

```python
mono = pd.DataFrame({"t": np.arange(1, 11), "g": np.exp(np.arange(1, 11))})
pear = ...    # Pearson corr of t and g
spear = ...   # Spearman corr of t and g

assert np.isclose(spear, 1.0)
assert pear < 0.8
```

In a comment: `g` is completely determined by `t` — why is Pearson so far from 1?

---

**Exercise 7.4** — seaborn on your own Axes.

```python
rng = np.random.default_rng(1)
plot_df = pd.DataFrame({"group": np.repeat(["a", "b", "c"], 50),
                        "value": np.concatenate([rng.normal(m, 1, 50) for m in (0, 2, 4)])})

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# Left: histogram of "value", one colour per group, titled "Distribution by group".
# Right: box plot of "value" per group, titled "Spread by group".
...

assert axes[0].get_xlabel() == "value"
assert axes[0].get_title() == "Distribution by group"
assert axes[0].get_legend() is not None
assert axes[1].get_title() == "Spread by group"
assert [t.get_text() for t in axes[1].get_xticklabels()] == ["a", "b", "c"]
```

Then a heatmap of `data.corr()` from 7.3, with the numbers written in each cell and the colour scale fixed to [−1, 1]:

```python
fig, ax = plt.subplots()
...

assert len(ax.texts) == 9
```

---

**Exercise 7.5** — Outliers by the IQR rule.

```python
v = pd.Series([10, 12, 11, 13, 12, 95, 11, 14, 13, -40])

q1, q3 = ...
iqr = ...
lo, hi = ...
outliers = ...

assert (q1, q3) == (11.0, 13.0)
assert (lo, hi) == (8.0, 16.0)
assert sorted(outliers.tolist()) == [-40, 95]
```

Predict: `v.mean()` vs `v.median()`. Which one describes a "typical" value here, and why?

---

# SECTION 8 — SQL with DuckDB
*Skills: SELECT/WHERE/ORDER, GROUP BY/HAVING, joins, window functions, NULL*

**Setup:** `make_orders()` (Section 4), `make_customers()` and `make_categories()` (Section 5), then:

```python
import duckdb

orders, customers, categories = make_orders(), make_customers(), make_categories()
```

Each task: write the SQL in `duckdb.sql("""...""").df()`.

---

**Exercise 8.1** — SELECT, WHERE, ORDER BY.

```python
res = ...   # order_id, customer, amount of books orders with a known amount, largest first

assert res["order_id"].tolist() == [5, 1, 3]

pd_version = ...   # the same result with pandas only
assert pd_version["order_id"].tolist() == res["order_id"].tolist()
```

---

**Exercise 8.2** — GROUP BY and HAVING.

```python
res = ...   # per customer: total amount and number of orders (as n_orders),
            # only customers whose total is above 100, largest total first

assert res["customer"].tolist() == ["piotr", "anna"]
assert res["total"].tolist() == [180.0, 145.0]
assert res["n_orders"].tolist() == [2, 3]
```

In a comment: why can't the condition go in `WHERE`?

---

**Exercise 8.3** — LEFT JOIN and COALESCE.

```python
res = ...   # every customer with city and total amount (0 if no orders),
            # largest total first, ties broken by customer name

assert res["customer"].tolist() == ["piotr", "anna", "jan", "ewa", "ola"]
assert res["total"].tolist() == [180.0, 145.0, 30.0, 15.0, 0.0]
```

---

**Exercise 8.4** — Window functions: the top row per group.

```python
res = ...   # each customer's single largest order (customer, order_id, amount), sorted by customer.
            # Use ROW_NUMBER() in a CTE; missing amounts must never win.

assert res["order_id"].tolist() == [6, 4, 7, 2]

pd_top = ...   # the same with pandas (hint: sort, then groupby().head(1))
assert pd_top["order_id"].tolist() == res["order_id"].tolist()
```

---

**Exercise 8.5** — Running totals.

```python
res = ...   # every order (by order_id) with running_total: the customer's cumulative amount so far

assert res["running_total"].tolist()[:7] == [40.0, 120.0, 65.0, 15.0, 180.0, 145.0, 30.0]

pd_run = ...   # the same running total with pandas groupby
```

Predict: the last row (ewa's order with a missing amount) in SQL vs pandas. They differ — explain why in a comment.

---

**Exercise 8.6** — NULL. Predict every result before running:

```python
duckdb.sql("SELECT COUNT(*) AS n_rows, COUNT(amount) AS n_amount FROM orders").df()   # predict
len(duckdb.sql("SELECT * FROM orders WHERE amount = NULL").df())                      # predict
len(duckdb.sql("SELECT * FROM orders WHERE amount IS NULL").df())                     # predict
duckdb.sql("SELECT AVG(amount) AS avg FROM orders").df()                              # predict: same as orders["amount"].mean()?
```

Then query a file directly — DuckDB reads Parquet without loading it into pandas first:

```python
import tempfile, pathlib

with tempfile.TemporaryDirectory() as tmp:
    path = pathlib.Path(tmp) / "orders.parquet"
    orders.to_parquet(path)
    n = ...   # COUNT(*) straight from the file: FROM 'path/to/file.parquet'
    assert n == 8
```

---

*Last updated: 2026-09-29*
