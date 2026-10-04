# Phase 1 — Mastery Log

Depth of load-bearing concepts, backed by evidence. Separate from `phase1/README.md`, which tracks completion. Scale and definitions: `docs/mastery/phase0.md`.

## 1A — pandas & SQL

- **Index alignment (label vs. positional arithmetic, NaN → float upcast)** — *Understood*, 2026-10-01. Ex 1.1: predicted index, values and dtype of both `s1 + s2` and `s1 + s2.to_numpy()` correctly. First explanation was wrong: "float because we are adding two Series" (`s1 + s1` stays `int64`). After two rounds of prompting, restated the full chain: labels only on one side → `NaN` → `int64` can't hold it → `float64`. Also explained, on the first attempt, why `add(..., fill_value=0)` stays `float64` (NaN is created during realignment, before the fill, and isn't cast back).
- **`df["col"]` vs `df[["col"]]` (key type decides Series vs DataFrame)** — *Understood*, 2026-10-02. Ex 1.2: predictions right. First explanation was wrong ("inner brackets make a 2-D array"). After correction, applied the rule correctly to `books[["title", "price"]]`. Why `books["title", "price"]` fails (a tuple is looked up as one label → `KeyError`) was only half-explained and then given by Claude.
- **One dtype per column vs. one per array (`to_numpy()` upcasting)** — *Understood*, 2026-10-02. Ex 1.3: dtypes predicted correctly. Used `include=["int", "float"]`, which misses unsigned ints; `"number"` recommended. Predicted `to_numpy()` → `object` correctly, but the reason started vague ("can't find better dtype") until Claude filled in why no numeric dtype fits text. Then applied it correctly to a new case: `[["year", "price"]].to_numpy()` → `float64`, with the reason.
- **Sorting and ranking (`sort_values`, `nlargest`, `rank` ties)** — *Understood*, 2026-10-04 (*Practiced* 2026-10-02). Ex 1.4 correct; `describe()` labels predicted correctly. `nlargest` not in the reading — needed a docs pointer. Why `rank` is always `float64`: first explanation wrong ("float because there's a tie" — `pages_rank` had no ties and was still `float64`); second half-right ("avoid dtype changing dynamically") but missed the mechanism. Full answer given by Claude: default `method="average"` gives tied rows the mean of their positions (2.5), so the output dtype must hold halves for any input. Tie values not predicted before running. Re-check 2026-10-04, unprompted and correct: `pd.Series([5, 5, 5]).rank()` → `2.0` ×3, `float64` because averaging can produce fractions.
- **CSV vs Parquet (schema survives a round trip)** — *Practiced*, 2026-10-02. Ex 1.5: predicted all four dtypes correctly. Needed the exercise structure walked through; errors along the way: reading before writing, `pd.from_parquet`, index written to the CSV, `parse_dates=True` (parses the index, not columns — explained by Claude). Reason for Parquet first given as "industry standard"; then "stores exact data types" — accepted. Follow-up (`fixed["format"]` dtype) answered by Claude.

## DSA track

- **Hash set/dict lookup cost vs. total cost** — *Practiced*, 2026-10-03. Contains Duplicate solved alone, optimal. Predicted the list version is $O(n^2)$ with the right reason (linear scan per check). First explanation of the set version said one lookup is $O(n)$ "because of hash"; corrected by Claude to $O(1)$ average per lookup × $n$ iterations. Raised a real question unprompted: the ord-sum hash makes "fe"/"ja" collide — led to collisions + equality check in hash tables, explained by Claude. Check question (why count dicts give no false positives) not answered.
- **Space complexity** — *Practiced*, 2026-10-03. Needed an explanation of what space measures. Valid Anagram: answered "O(104)" — two errors (a constant inside Big-O; sizing the dict by input length instead of distinct keys). $O(1)$ for a 26-letter alphabet and $O(n)$ for the Unicode follow-up explained by Claude, not derived. Re-check on the next problem.
- **Big-O vs. constant factors** — *Exposed*, 2026-10-03. Noticed his $O(n)$ dict version ran slower than `sorted` on LeetCode; explanation (C vs. Python per-step cost, crossover between 100 and 10,000 chars, benchmarked) given by Claude.

---

*Last updated: 2026-10-04*
