# Phase 0 — Foundations: Python · NumPy · Math

This folder holds the actual teaching content and drills for Phase 0. The
plan, deadlines, and project specs live one level up (`docs/ROADMAP.md`,
`docs/phase0/projects.md`); this is where the material itself lives.

> **The philosophy of this phase:** Phase 0 is not about memorizing syntax.
> It is about building mental models that will still be correct in 3 years.
> Every concept here will reappear — in PyTorch, in transformer code, in
> distributed training. Do it right now or pay the debt later with interest.

---

## What's in here

| File | Content |
|------|---------|
| `python_concepts.md` | Python fundamentals, OOP, functions, error handling, types, project structure. Read this, don't drill it. |
| `python_exercises.md` | ~70 Python drill exercises across 7 sections, plus Git/GitHub drills. Predict-before-run methodology — do these. |
| `numpy_concepts.md` | NumPy mindset, indexing, broadcasting, vectorization, linear algebra ops, einsum, numerical stability. |
| `numpy_exercises.md` | ~60 NumPy drill exercises across 8 sections. Same predict-before-run methodology. |
| `matplotlib_concepts.md` | Figure/Axes anatomy, plot types, subplots, log scale, heatmaps, saving figures. |
| `math_concepts.md` | Linear algebra, calculus/backprop intuition, and probability, connected directly to ML code. |
| `habits_and_tools.md` | Engineering habits, math-to-code habits, learning habits, editor setup. Applies throughout, not section-specific. |

Projects (CLI Weather Tool, Data Pipeline, Linear Regression from Scratch,
NumPy Neural Network, plus stretch) are specified separately in
`docs/phase0/projects.md` — not duplicated here.

---

## How to Structure Your Time

Target: ~8 weeks (started 2026-08-03, target date 2026-09-27 — see
`docs/ROADMAP.md`), 3–4 hours/day = roughly 170–220 hours.

**Each study session:**
- 15 min — review yesterday's notes or code. Fix anything that felt unclear.
- 60–90 min — new concept: read, watch, understand.
- 60–90 min — code it. Not copy-paste. Type it yourself, break it on purpose, fix it.
- 15 min — write one paragraph explaining what you learned in plain language, as if teaching a friend. If you cannot explain it simply, you do not understand it yet.

**Each week:**
- Monday–Friday: new content
- Saturday: build or extend the week's project
- Sunday: review the week, fill gaps, push clean code to GitHub

Rule: never leave a session without committing something to Git — see `docs/GIT_GUIDE.md`.

---

## Phase 0 Completion Checklist

Go through this honestly before moving to Phase 1. "I sort of know this" is not the same as "I can do this without looking anything up."

### Python
- [ ] Can write a class with `__init__`, instance variables, properties, `@staticmethod`, `@classmethod`, and relevant dunder methods from memory
- [ ] Can explain in words (not code) the difference between an instance and a class variable, with a concrete example
- [ ] Can write a closure and explain what it captures and why it works after the outer function ends
- [ ] Can explain how a decorator works mechanically — not just how to use the `@` syntax
- [ ] Can write a generator function and explain why it uses less memory than returning a list
- [ ] Uses type hints on every function in every project
- [ ] Uses `logging` instead of `print` in all project code
- [ ] Every project is in a Git repo with a clean, meaningful commit history
- [ ] Can structure a multi-file Python project with proper package imports
- [ ] Can write and run `pytest` tests

### NumPy
- [ ] Given any two array shapes, can immediately say whether they broadcast and what the output shape is
- [ ] Can implement any mathematical formula in vectorized NumPy — no Python loops over array elements
- [ ] Knows the difference between a view and a copy, and can predict which operations produce which
- [ ] Can use `np.einsum` for at least matrix multiplication and dot products
- [ ] Has completed the core projects (see `docs/phase0/projects.md`)

### Math
- [ ] Can write the MSE loss formula, differentiate it with respect to w, and implement the result in NumPy — all from scratch without references
- [ ] Can explain in plain language what an eigenvalue represents geometrically
- [ ] Can implement softmax and cross-entropy from scratch in NumPy without looking up the formulas
- [ ] Can explain the connection between cross-entropy loss and maximum likelihood estimation
- [ ] Can implement gradient descent from scratch and explain what each line does and why
- [ ] Can implement k-means clustering from scratch in NumPy
- [ ] Can apply Bayes' theorem to compute a posterior from a prior and a likelihood, and explain expectation/variance/covariance in plain language

**When all of these feel solid — not just familiar, but solid — you are ready for Phase 1.**

---

*Last updated: 2026-08-18*
