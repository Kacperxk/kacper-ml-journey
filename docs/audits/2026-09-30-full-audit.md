# Repository Audit — 2026-09-30 (Phase 1 start, Phase 0 close-out)

Fifth audit, since 2026-09-27. Scope: Phase 1 docs (`docs/phase1/`, `phase1/`), global docs (`docs/*.md`, `README.md`, `CLAUDE.md`, `docs/dsa/`), and `ROADMAP.md` staleness, then a final run of everything in `phase0/`.

## A. Module 1A drills verified

All 41 exercises in `pandas_exercises.md` were solved with throwaway reference solutions (not committed) and run against pandas 3.0.6, DuckDB 1.5.6, seaborn 0.13.2. Every setup cell runs and every assert passes. Every *Predict* item behaves as its prompt implies: the precedence bug in 2.2 raises `TypeError`, chained assignment in 2.3 warns with `ChainedAssignmentError`, writing to `to_numpy()` in 2.4 raises `ValueError`, `pivot` in 6.2 raises `ValueError`, SQL vs pandas running totals in 8.5 differ (15.0 vs NaN).

The pandas 3 claims in `pandas_concepts.md` were also checked against pandas 3.0.6: `"M"` frequency rejected, `SettingWithCopyWarning` removed, `observed=True` default, grouping columns excluded from `groupby().apply()`, missing strings as `NaN`, inferred datetime resolution (`datetime64[us]`). McKinney's online edition states it's updated for pandas 2.0.0, as the doc says. Géron (2025) chapter numbers in the reading map match the book's repo.

## B. Problems found and fixed

- **Ex 1.3 used `select_dtypes` without it being taught** (authoring rule 2), and the obvious pre-pandas-3 answer, `include="object"`, now emits a deprecation warning. Note added to `pandas_concepts.md` Section 1.
- **`ROADMAP.md` month-by-month table was off by one month.** Phase 0 took months 1–2 (Aug–Sept), but the table had it as month 1 and Phase 1 as months 2–3. Shifted the table by one month, added "Month 1 = August 2026", and updated Phase 5's start and interview prep to match (~16, 15–16). `docs/dsa/README.md`'s "month 14–15" updated to 15–16, which also matches its own 14-month estimate from Sept 28.
- **`ROADMAP.md` listed CatBoost under 1E**, but `docs/phase1/README.md` and `requirements.txt` don't include it. Removed from the roadmap. "Section 1B" corrected to "Module 1B".
- **`GIT_GUIDE.md` duplicated `.gitignore` and had drifted from it**: the copy was missing `.mypy_cache/`, `.pytest_cache/` and the `sample.jsonl` exception. Replaced with a pointer and a short data rule, which matters now that Phase 1 uses real datasets.
- **1F reading map omitted SVMs.** In Géron (2025) they're in Appendix C, not ch. 7–8. Added.
- `REPO_STRUCTURE.md` said `requirements.txt` was populated only for Phase 0. Corrected.
- `requirements.txt` listed scikit-learn for Phase 1 only, but Phase 0 Project 3 imports it (`fetch_california_housing`). Comment updated.

## B2. Phase 0 close-out

Everything in `phase0/` re-run on the current `.venv` (numpy 2.5.1, matplotlib 3.11.1):

- **All pass:** 7 Python section files (section 7 also run in an empty directory, without the untracked `data.csv`), 8 NumPy notebooks and both `notebooks/` executed with `nbconvert`, Project 2's 6 pytest tests, the `run_experiments` scripts for Projects 3, 4 and `microtensor`, and a live Weather Tool call (valid city, plus an invalid city giving the clean one-line error).
- **Project 3 is flaky:** synthetic data isn't seeded, so 2 of 25 runs failed `np.allclose(true_w, model_cf.w, atol=0.1)` on sampling noise. Kacper's code, left as is. Recorded in the project README.
- **Project 3 vs. its spec:** "done when" asks closed-form and GD to agree within 0.01; the script checks each against the true weights at 0.1 instead.
- **`microtensor`:** the mastery log's "all 12 gradients reproduced" re-checked. All 12 match `TwoLayerNet.backward()`; the committed script asserts 2.
- **Project READMEs** added for Projects 3, 4 and `microtensor` (open item since 2026-09-27), in the format of Projects 1–2, with numbers from these runs.
- All 21 tags (15 sections, 4 projects, stretch, `phase0-complete`) present on `origin`.

## C. Pace

- **Phase 1:** day 3 of 63. Module 1A (1.5 wk, nominally Sept 28 – Oct 8): 0/8 sections done. Sept 28–29 went into planning and writing the module docs, so 8 sections are left for ~9 days.
- **Phase 1 budget is over by ~0.5 week before Project 2.** Modules add up to 7.5 weeks, Project 1 is a few days, and the capstone is 1.5 weeks. That's ~9.5 weeks in a 9-week window, and Project 2 runs across 1D–1E on top of those modules. The probability midterm on Dec 4 also competes with the last week.
- **DSA:** started 2026-09-28. Block 0 (Big-O, pythonds3 ch. 2) not started, 0 problems. Expected pace is 1 reading + 2–3 problems/week, so block 0 is due this week.

## D. Decisions and open items

Decided by Kacper, 2026-09-30:

- **No Phase 1 scope cuts for now**, despite the overrun in C.
- **1B assumes no probability background.** The uni course isn't assumed to have covered anything; 1B teaches random variables, expectation/variance, distributions and likelihood from Blitzstein & Hwang. `docs/phase1/README.md` updated. This adds material to a 1-week module, which makes the overrun in C worse.
- **DSA block 0:** Kacper will fit it in this week.

Open (Kacper's):

- **Project 3 flaky assert**: seed the synthetic data (e.g. `np.random.default_rng(0)`).
- **Commit author name:** set the same global `user.name` (`Kacper Badowicz`) on the other machine.
- **Phase 0 Completion Checklist** (`docs/phase0/README.md`): 22 items, unticked.

## E. Checked, nothing found

`main` is in sync with `origin`; all tags pushed, including `phase0-complete`. The `.venv` (Python 3.13.15) has every `requirements.txt` package at or above its floor, and `pip check` is clean. `README.md`, `CLAUDE.md`, `phase1/README.md` status and dates are current. Exercise count (41) matches the header. `phase2/`–`phase4/` placeholders unchanged.

---

*Audit conducted and resolved: 2026-09-30*
