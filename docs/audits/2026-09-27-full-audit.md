# Full Repository Audit — 2026-09-27 (Phase 0 close)

Fourth audit, since 2026-09-23. Scope: the stretch project's build, and a phase-end staleness sweep of every doc, since Phase 0 closes today.

## A. Phase 0 summary

Started 2026-08-03 and completed 2026-09-27, on the target date. Delivered: 7 Python sections (24 exercises), 8 NumPy sections (36 exercises), 4 core projects (Weather Tool, Data Pipeline, Linear Regression, NumPy Neural Network), and 1 stretch project (Scalar Autograd Engine, `microtensor`). Cut: the other three stretch projects, dropped deliberately on 2026-09-23 so the remaining time went into one project that reinforced backpropagation. Every section and project is tagged; `phase0-complete` marks the end.

From `docs/mastery/phase0.md`: backpropagation was the hardest concept of the phase and is now *Verified* twice, once through Project 4's hand-derived backward pass and once through `microtensor` reproducing those same gradients automatically. Probability foundations (distributions, expectation/variance, Bayes) are still only *Exposed*: written into `math_concepts.md` 1.3 but never exercised by any project. That's the weakest area going into Phase 1. Keeping the computational graph connected is marked fragile, since the same mistake happened twice.

## B. What changed since the last audit

`microtensor` went from a spec to a complete, verified project: a `Value` class with six operations and `backward()` via topological sort, all arithmetic dunders, `Neuron`/`Layer`/`MLP`, a check reproducing all 12 of Project 4's hand-derived gradients, a gradient-accumulation check, and a tiny MLP trained on XOR (loss 4.13 → ~0). Moved from the planned `stretch/` subfolder to `phase0/projects/microtensor/`, since a subfolder holding one project added nothing. Tagged `p0-stretch-microtensor`.

## C. Problems found and fixed

**Spec errors caught while building.** The spec asked for a check against Project 4's softmax/cross-entropy example without specifying `exp`/`log`, so that check couldn't be written as specified. Added both (2026-09-26). The spec also told `Neuron` to use Project 4's `0.01` init scale, which left a 3-layer MLP stuck at its starting loss. Tested before building on it, and corrected to `uniform(-1, 1)` (2026-09-27). The dunder list was also missing `__rtruediv__`, which was built; added to the spec.

**Staleness that earlier audits missed.** `REPO_STRUCTURE.md` and the two exercise files' own headers still said "~70" Python and "~60" NumPy exercises. The 2026-09-05 audit fixed those counts in `ROADMAP.md` and `docs/phase0/README.md` but not in these three places. Corrected to the verified 24 and 36. `REPO_STRUCTURE.md` was also missing the two project write-up PDFs in `docs/phase0/`, `notebooks/matplotlib_practice.ipynb`, `.python-version`, and every audit after the first. The audits entry is now a filename pattern, so it won't go stale again.

**`CLAUDE.md`.** Its git-identity note said the 18-commit misattribution was "caught 2026-08-05," but those commits actually stayed wrong until the 2026-09-13 rewrite. Corrected, and added an explicit rule: when committing for Kacper, take the name/email from `git config --global` or `git log`, never from conversation context. Phase status, source-of-truth descriptions, and the deadline-pacing rule updated from Phase 0-specific wording.

**Mastery log.** Two entries were out of date by the end of the phase. Cross-entropy was still "not yet Applied," though it has since been used in Project 4's training loop and rebuilt in `microtensor`. The probability entry's "first real test in Project 4" had passed without the test happening; now recorded honestly as still *Exposed*.

**Phase-completion status** updated consistently across `phase0/README.md`, root `README.md`, `ROADMAP.md`, `REPO_STRUCTURE.md`, `docs/phase0/README.md`, and `projects.md`. The stretch list now records the outcome (1 of 4 built) instead of leaving three unchecked boxes that looked like unfinished work.

## D. Open items (Kacper's, not fixed here)

- **Phase 0 Completion Checklist** (`docs/phase0/README.md`): 22 self-assessment items, all unticked. Phase 0 was marked complete with it open, by Kacper's decision (2026-09-27). It's a self-check, not a gate, and only Kacper can honestly tick it.
- **Project READMEs:** Projects 1 and 2 have their own `README.md`, as `REPO_STRUCTURE.md`'s convention expects; Projects 3, 4 and `microtensor` don't. The two PDFs in `docs/phase0/` partly cover 3 and 4.
- **Commit author name** varies by machine: `Kacper` (almost all commits), `Kacper Badowicz` (9), `Kacperxk` (2). All share the correct email, so GitHub attribution is fine. Setting the same `git config --global user.name` on both machines would stop it.
- **Unpushed commits:** 8 code commits plus this close-out, and all tags including `p0-stretch-microtensor` and `phase0-complete`. Push with `git push && git push --tags`.

## E. Checked, nothing found

`.gitignore` is still effective: no `__pycache__/`, `.pytest_cache/`, `figures/`, or `output/` content tracked. Every tag is annotated, and there's one per section and project, with no duplicates. `requirements.txt` needed nothing new (`microtensor` uses only `math` and `random`). No Phase 1 content was created; `phase1/`–`phase4/` stay as placeholders.

---

*Audit conducted and resolved: 2026-09-27*
