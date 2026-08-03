# CLAUDE.md

This is `ml-engineering-course` (GitHub: Kacperxk/kacper-ml-journey) — Kacper's self-directed ML engineering curriculum. This file is the entry point for any Claude session working in this repo. Read it first.

## What this repo is
An 18-month, 6-phase self-study curriculum toward ML engineering, currently in Phase 0 (Python/NumPy/Math foundations). Full plan: `docs/ROADMAP.md`. Current phase's project specs: `docs/PHASE0_PROJECTS.md`. Git workflow/conventions: `docs/GIT_GUIDE.md`.

## Working style — read this before writing any code
Kacper wants Claude as a trainer/helper, not a replacement worker. No vibecoding — do not write whole apps, projects, or exercise solutions for him. He wants explanations, help with debugging, refactoring feedback, and code review. When he's working through an exercise or project from `docs/PHASE0_PROJECTS.md`, guide and critique rather than hand him a finished implementation, unless he explicitly asks for a full solution (e.g. to compare against his own after he's already tried it).

He's doing this for himself, not for anyone else — avoid superlatives or self-promotional framing about him (e.g. "ambitious," "excellent," "amazing exam result") anywhere in this repo's docs. He learns by digging into *why* something works rather than memorizing, and likes things tracked and structured — hence this whole restructuring effort. He's a 2nd-year Econometrics & Data Science student at University of Warsaw, not a CS/ML student, teaching himself this material outside his degree.

## Current state (as of 2026-08-03)
The restructuring described below is **done**, in a new commit on top of the original initial commit (which had the old structure: three independent, overlapping project lists, duplicated/conflicting git guidance, a likely-fabricated model name "Mythos" in the old roadmap).

**Completed this session:**
1. `docs/ROADMAP.md`, `docs/PHASE0_PROJECTS.md`, `docs/GIT_GUIDE.md`, `docs/REPO_STRUCTURE.md`, `docs/MERGE_INSTRUCTIONS.md` are all in place under `docs/`.
2. Root `README.md` refreshed to match the scoped commit convention and link to `docs/`.
3. Folder structure rebuilt per `docs/REPO_STRUCTURE.md`: `phase0/python/` (7 stub files), `phase0/numpy/` (8 stub files), `phase0/projects/{weather_tool,data_pipeline,linear_regression,numpy_neural_net,stretch/{preprocessing_engine,config_manager,microtensor,mini_ml}}` all scaffolded with docstring-only stubs pulled from `docs/PHASE0_PROJECTS.md`. No `sklearn_pandas/` existed yet, so nothing to rename there.
4. `phase0/README.md` is now a living checklist (done/in-progress/next), not exercise text.
5. Committed as `refactor(structure): consolidate roadmap and project docs into docs/`.

**Confirmed:** Kacper wants Project 3 kept as the combined "Linear Regression from Scratch + Gradient Descent Visualizer" — no split needed. This is locked in.

**Still open — blocks part of the merge:** `docs/MERGE_INSTRUCTIONS.md` calls for deleting superseded sections from `phase0_complete.md`, `python_exercises.md`, `numpy_exercises.md` and moving their concept/exercise content into `docs/phase0/`, plus deleting `ml_course_repo_structure.md` / `ml_engineer_roadmap.md`. None of these old files exist anywhere in the repo or uploads — Kacper confirmed he hasn't uploaded them yet and will when asked. Until then, `phase0/python/*.py` and `phase0/numpy/*.py` only have topic-title docstrings (no real problem statements), and `docs/phase0/` doesn't exist yet. **Next session: ask Kacper to upload those 5 files, then finish this step** (extract concept + exercise content into `docs/phase0/`, fill in real docstrings, delete the old files, delete `docs/MERGE_INSTRUCTIONS.md` once its checklist is fully done).

## Conventions
- Commit messages: `type(scope): description` — see `docs/GIT_GUIDE.md` for the full convention and examples. Don't use the old unscoped style.
- Docs vs code split: `docs/` holds planning and instructional material (roadmap, project specs, concept explanations, exercise problem statements). Phase folders (`phase0/`, `phase1/`, ...) hold only code and a short status README. Don't let exercise prose creep back into the code folders.
- Phase 0 has a hard deadline: **September 27, 2026**. If behind schedule, cut scope (drop a stretch project, skip exercises he's already comfortable with) rather than let the date slip.
