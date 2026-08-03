# Merge Instructions

What to do with the 4 new files (`ROADMAP.md`, `PHASE0_PROJECTS.md`, `GIT_GUIDE.md`, `REPO_STRUCTURE.md`) relative to what you already have. Nothing here needs to happen automatically — this is a checklist for you to work through once the repo is on your Mac.

## What prompted this

You had 4 documents (`ml_course_repo_structure.md`, `ml_engineer_roadmap.md`, `numpy_exercises.md`, `python_exercises.md`, plus `phase0_complete.md`) generated somewhat independently. Individually they're good — the exercises and concept explanations are genuinely well-built and should NOT be rewritten. The problem was structural: three of them each defined their own "Phase 0 projects" list (9 projects total), only one of those lists (3 projects) was ever wired into the actual repo folder structure, and git setup instructions were duplicated three times with two different, conflicting commit conventions. `ml_engineer_roadmap.md` also referenced an Anthropic model called "Mythos" that I can't verify is real — likely something the model that generated it invented.

## Keep unchanged (these are good as-is)

- `phase0_complete.md` **Parts 1–3** (Python concepts, NumPy concepts, Math) — no changes needed, this is solid teaching content.
- `numpy_exercises.md` **Sections 1–8** (the ~60 drill exercises) — no changes needed.
- `python_exercises.md` **Sections 1–7** (the ~70 drill exercises) — no changes needed.

## Delete / replace

- `phase0_complete.md` **Part 4 "Projects"** (Project 0.1, 0.2, 0.3) — delete this section. Superseded by `PHASE0_PROJECTS.md`. Projects 0.1 and 0.3's content is preserved there (0.1 became Core Project 1, 0.3 became a stretch project); 0.2 was merged into Core Project 3.
- `phase0_complete.md` **§1.7 "Git: Start Today"** — delete, replace with a one-line pointer: "See `GIT_GUIDE.md` for the full workflow."
- `python_exercises.md` **"PROJECT 1 — Configuration Manager"**, **"PROJECT 2 — Data Pipeline"**, **"PROJECT 3 — Mini ML Framework"** — delete these sections. Data Pipeline became Core Project 2 (moved, not lost). Config Manager and Mini ML Framework became stretch projects — full specs preserved there if you decide to do them later.
- `python_exercises.md` **Section 8 "Git and GitHub Drills"** — delete, replace with a pointer to `GIT_GUIDE.md`. (The actual hands-on drills in §8.1–8.6 are fine to keep if you want practice reps on git commands specifically — just note they now use the commit convention from `GIT_GUIDE.md`, not the unscoped one originally shown.)
- `numpy_exercises.md` **"PROJECT 1 — Data Preprocessing Engine"**, **"PROJECT 2 — Gradient Descent Visualizer"**, **"PROJECT 3 — NumPy Neural Network"** — delete these sections. Preprocessing Engine became a stretch project. Gradient Descent Visualizer was merged into Core Project 3. NumPy Neural Network became Core Project 4 (unchanged in substance, just relocated).
- `ml_course_repo_structure.md` and `ml_engineer_roadmap.md` — replace entirely with `REPO_STRUCTURE.md` and `ROADMAP.md`.

## New files to add to the repo root

- `ROADMAP.md`
- `PHASE0_PROJECTS.md`
- `GIT_GUIDE.md`

Then use `REPO_STRUCTURE.md` as the reference when you actually create the `phase0/projects/` folders — rename any existing `sklearn_pandas/` references to `classical_ml/` if you'd already started phase1 scaffolding.

## One judgment call left to you

`PHASE0_PROJECTS.md` merges "Linear Regression from Scratch" and "Gradient Descent Visualizer" into one project. If you'd rather keep them as two separate, smaller projects instead of one combined one, that's a completely reasonable call — the content is the same either way, just split differently. Say the word and I'll split it back out.

---

*Last updated: 2026-08-03*
