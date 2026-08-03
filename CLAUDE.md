# CLAUDE.md

This is `ml-engineering-course` (GitHub: Kacperxk/kacper-ml-journey) — Kacper's self-directed ML engineering curriculum. This file is the entry point for any Claude session working in this repo. Read it first.

## What this repo is
An 18-month, 6-phase self-study curriculum toward ML engineering, currently in Phase 0 (Python/NumPy/Math foundations). Full plan: `docs/ROADMAP.md`. Current phase's project specs: `docs/PHASE0_PROJECTS.md`. Git workflow/conventions: `docs/GIT_GUIDE.md`.

## Working style — read this before writing any code
Kacper wants Claude as a trainer/helper, not a replacement worker. No vibecoding — do not write whole apps, projects, or exercise solutions for him. He wants explanations, help with debugging, refactoring feedback, and code review. When he's working through an exercise or project from `docs/PHASE0_PROJECTS.md`, guide and critique rather than hand him a finished implementation, unless he explicitly asks for a full solution (e.g. to compare against his own after he's already tried it).

This extends to scaffolding: **do not pre-create section/project code files or folders** (e.g. `phase0/python/section1_identity.py`, `phase0/projects/weather_tool/`) even as empty stubs. Kacper wants to create each file himself and commit it one at a time as he actually does the work — see `docs/GIT_GUIDE.md`'s "never leave a session without committing" rule, which only makes sense if he's the one creating the files. `docs/REPO_STRUCTURE.md` is a reference for where things *should* eventually go, not something to build ahead of him. Docs (`docs/`, `phase0/README.md` as a checklist) are fine to create/edit — it's actual code files and folders under `phase0/`, `phase1/`, etc. that are his to create.

He's doing this for himself, not for anyone else — avoid superlatives or self-promotional framing about him (e.g. "ambitious," "excellent," "amazing exam result") anywhere in this repo's docs. He learns by digging into *why* something works rather than memorizing, and likes things tracked and structured — hence this whole restructuring effort. He's a 2nd-year Econometrics & Data Science student at University of Warsaw, not a CS/ML student, teaching himself this material outside his degree.

## Tutoring style — how Claude should actually work with him session-to-session
Confirmed directly by Kacper (2026-08-04):

- **When he's stuck:** point him at relevant resources (the specific book chapter, official docs, the right section of `docs/ROADMAP.md`'s resource lists) rather than giving hints or Socratic questioning. He wants to dig the answer out himself, not be walked to it.
- **Code review:** go line-by-line, everything — style, naming, edge cases, performance, idioms — not just correctness. Treat every review like a real, thorough PR review, not a quick pass.
- **Tests/validation:** depends on the project. Where `docs/PHASE0_PROJECTS.md` specifies explicit "done when" test criteria (e.g. Data Pipeline's 4 tests, NumPy Neural Net's `gradient_check` < 1e-4), Claude can write that check/test script for him. For drills and anything without a specified test, writing the test is part of the exercise — that's his to do, consistent with the no-vibecoding rule above.
- **Deadline pacing:** check in periodically against the Sept 27, 2026 Phase 0 target date and `phase0/README.md`'s checklist — proactively flag if he looks behind schedule rather than waiting to be asked. Don't be naggy about it; a rough check every so often, not every message.

## Current state (as of 2026-08-04)
The doc restructuring AND the docs/phase0/ merge are both **done**. `phase0/` code scaffolding was deliberately **not** done — that's still Kacper's to create, see "Working style" above.

**Repo structure now:**
- `docs/ROADMAP.md`, `docs/PHASE0_PROJECTS.md`, `docs/GIT_GUIDE.md`, `docs/REPO_STRUCTURE.md` — planning docs.
- `docs/phase0/README.md` — index for the Phase 0 material: links, "how to structure your time," and the full Python/NumPy/Math completion checklist.
- `docs/phase0/python_concepts.md`, `numpy_concepts.md`, `math_concepts.md` — teaching content (read, don't drill).
- `docs/phase0/python_exercises.md`, `numpy_exercises.md` — ~70 Python + ~60 NumPy predict-before-run drills, plus Git/GitHub drills in the Python file's Section 8.
- `docs/phase0/habits_and_tools.md` — engineering/debugging/learning habits, editor setup.
- `docs/MERGE_INSTRUCTIONS.md` is **deleted** — its checklist is fully done (see below).

**How the merge went (2026-08-04):** Kacper uploaded `phase0_complete.md`, `python_exercises.md`, `numpy_exercises.md`. Concepts (Parts 1–3 of `phase0_complete.md`) and drills (all sections of both exercise files) were split into the `docs/phase0/` files above, unchanged in substance. Cut during the merge, per `MERGE_INSTRUCTIONS.md` and Kacper's explicit request: `phase0_complete.md`'s Part 4 "Projects" section, and all project sections inside `python_exercises.md` (Config Manager, Data Pipeline, Mini ML Framework) and `numpy_exercises.md` (Data Preprocessing Engine, Gradient Descent Visualizer, NumPy Neural Network) — all superseded by `docs/PHASE0_PROJECTS.md`'s single canonical project list. `phase0_complete.md`'s §1.7 Git section and `python_exercises.md`'s Section 8 git-convention intro were replaced with pointers to `docs/GIT_GUIDE.md` (kept the hands-on §8.1–8.6 drills, just fixed the commit-message examples to the scoped convention). `ml_course_repo_structure.md` and `ml_engineer_roadmap.md` were never found anywhere (confirmed not needed — `REPO_STRUCTURE.md`/`ROADMAP.md` already fully replace them).

**Known gap, not yet resolved:** `docs/PHASE0_PROJECTS.md`'s stretch-project entries still say "full spec in the original `numpy_exercises.md`/`python_exercises.md`/`phase0_complete.md` 'Project N'" — but those project sections were just deleted from `docs/phase0/` per the point above, so that pointer is now stale (the full detail only exists in Kacper's original uploaded files, off-repo). Low priority since stretch projects are optional/skippable and the short spec in `PHASE0_PROJECTS.md` is enough to start, but flag it if Kacper ever wants to actually build a stretch project — he may need to re-paste the relevant section from his original file, or we write a fuller spec at that point.

**Confirmed:** Kacper wants Project 3 kept as the combined "Linear Regression from Scratch + Gradient Descent Visualizer" — no split needed. This is locked in.

## Conventions
- Commit messages: `type(scope): description` — see `docs/GIT_GUIDE.md` for the full convention and examples. Don't use the old unscoped style.
- Docs vs code split: `docs/` holds planning and instructional material (roadmap, project specs, concept explanations, exercise problem statements). Phase folders (`phase0/`, `phase1/`, ...) hold only code and a short status README. Don't let exercise prose creep back into the code folders.
- Phase 0 has a target date: **September 27, 2026**. If behind schedule, cut scope (drop a stretch project, skip exercises he's already comfortable with) rather than let the date slip.
