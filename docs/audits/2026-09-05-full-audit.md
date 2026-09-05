# Full Repository Audit — 2026-09-05

First full audit under the mentor/curriculum-architect operating mode. Based on reading every doc in the repo, the full git history (130 commits, tags, branches), `.gitignore`, and spot-checks of code in `weather_tool/`, `data_pipeline/`, and `linear_regression/`.

## A. Current Architecture

Three layers, cleanly separated in intent: `docs/` (planning + teaching material), phase folders (code + a thin live-status tracker), and `CLAUDE.md` (operating rules for AI assistance in the repo). `docs/ROADMAP.md` is the single 18-month, 6-phase plan; `docs/phase0/` holds Phase 0's actual teaching content (one `*_concepts.md` + one `*_exercises.md` per subject, plus `math_concepts.md`, `habits_and_tools.md`, and `projects.md`); `phase0/README.md` is a lean, non-duplicated checklist of section/project completion. Git discipline is real: 130 commits, `type(scope): description` convention followed in all but 2 commits, tags for every completed section and project.

## B. Strengths — preserved, not rebuilt

- `phase0/README.md`'s lean, non-duplicated checklist style — the template for future phase trackers.
- CLAUDE.md's 7-rule exercise-authoring checklist — real, evidence-driven governance, each rule born from a caught failure.
- Math content already verified by execution (finite-difference gradient checks, numerical comparisons) before being written down, not asserted.
- Solid engineering practice in code: modern type hints, custom exceptions, generator-based laziness, `pytest` coverage, docstring-first development.

## C. Problems Found

**Structural**
- `.gitignore`'s blanket `*.jsonl`/`*.json` exclusion silently dropped `data_pipeline/sample.jsonl`, a needed fixture, not generated output.
- `GIT_GUIDE.md` mandated a feature branch per project; zero branches were ever used across 130 commits — documented workflow and actual practice had fully diverged.
- `docs/phase0/README.md` and `ROADMAP.md` both claimed "~70 Python" / "~60 NumPy" exercises; actual counts were 24 and 36.
- `.mypy_cache/` wasn't in `.gitignore` explicitly.

**Educational/curriculum (highest priority)**
`docs/ROADMAP.md`'s Starting Profile claimed "math foundation from econometrics coursework (linear algebra, calculus, probability/stats)," repeated twice more in the Phase 0 math section. This was factually wrong — econometrics hadn't been taken yet — and it caused a real, observable tutoring failure: repeated incorrect appeals to "you already know this from econometrics" while teaching linear regression, which had to be corrected mid-session. `math_concepts.md` 1.3 had no foundational treatment of what a probability distribution actually is, despite the roadmap explicitly promising coverage of Gaussian/Bernoulli/Categorical distributions — a real prerequisite gap, more serious than it first appeared given the corrected background.

**Documentation quality**
Generally strong; the one specific gap against the new standard was that no LaTeX was used anywhere for mathematical notation.

**Claude configuration**
CLAUDE.md had no rule requiring background/prerequisite claims to be verified against reality before being used pedagogically — directly how the econometrics error happened. Nothing yet encoded the exposed-vs-mastered distinction or permission to push back on superficial understanding.

## D–H. Proposed Architecture, Mastery System, Curriculum Fixes, Doc Standard

Delivered in full in the conversation this audit is drawn from — summarized in the Resolution section below with what was actually implemented.

## I. Migration Plan / Resolution

All items approved and implemented same-day (2026-09-05):

1. **`ROADMAP.md` Starting Profile corrected** — removed the false econometrics claim (replaced with the confirmed real background: dedicated Calculus and Linear Algebra coursework, zero Probability/Statistics), removed the personal biography subtitle, corrected the stale exercise counts (also fixed in `docs/phase0/README.md`).
2. **`math_concepts.md` rebuilt for probability, reviewed lightly for linear algebra/calculus.** Confirmed background (real Calculus and Linear Algebra courses, no Probability/Statistics) meant 1.1 and 1.2 needed only light additions — a partial-derivative/gradient bridge in 1.2 — while 1.3 needed a genuine from-zero foundation: random variables, PMF vs. PDF, Bernoulli, Categorical, and Gaussian distributions, each tied concretely back to material already covered (Categorical ↔ softmax, Bernoulli ↔ binary cross-entropy, Gaussian ↔ `np.random.randn` and the k-means synthetic-cluster generation). Scope decision (Kacper, 2026-09-05): this file should be the complete ML math-prerequisites reference, long where that adds real value, rather than deferring statistics coverage to Phase 1.
3. **`docs/mastery/phase0.md` created**, backfilled with evidence-specific entries from this session (NumPy Sections 7–8, Project 3 in progress) rather than retroactively guessing at earlier sections.
4. **`CLAUDE.md` updated**: added a rule to verify `ROADMAP.md`'s background claims before relying on them, a pointer to `docs/mastery/`, and explicit permission to push back on superficial or vague explanations rather than accepting them to keep pace. Also removed the file's own leftover biography specifics (university, year, program name), keeping only the operationally relevant fact (no formal CS/ML coursework).
5. **`.gitignore` fixed** — `sample.jsonl` allowed through via a targeted negation rule; `.mypy_cache/` and `.pytest_cache/` added explicitly.
6. **`GIT_GUIDE.md` branching section rewritten** to match actual practice. Decision (Kacper, 2026-09-05): keep committing straight to `main`, as done for all 130 commits so far — the documented per-project branching rule is dropped rather than newly enforced.
7. **`REPO_STRUCTURE.md` updated** to reflect the new `docs/mastery/` and `docs/audits/` directories.

No code under `phase0/`, `phase1–4/`, or `notebooks/` was touched — this was a documentation and process audit, not a code restructuring.

---

*Audit conducted and resolved: 2026-09-05*
