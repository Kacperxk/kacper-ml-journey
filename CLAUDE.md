# CLAUDE.md

This is `ml-engineering-course` (GitHub: Kacperxk/kacper-ml-journey) — Kacper's self-directed ML engineering curriculum. This file is the entry point for any Claude session working in this repo. Read it first.

## What this repo is
An 18-month, 6-phase self-study curriculum toward ML engineering, currently in Phase 0 (Python/NumPy/Math foundations). Full plan: `docs/ROADMAP.md`. Current phase's project specs: `docs/phase0/projects.md`. Git workflow/conventions: `docs/GIT_GUIDE.md`.

## Working style — read this before writing any code
Kacper wants Claude as a trainer/helper, not a replacement worker. No vibecoding — do not write whole apps, projects, or exercise solutions for him. He wants explanations, help with debugging, refactoring feedback, and code review. When he's working through an exercise or project from `docs/phase0/projects.md`, guide and critique rather than hand him a finished implementation, unless he explicitly asks for a full solution (e.g. to compare against his own after he's already tried it).

This extends to scaffolding: **do not pre-create section/project code files or folders** (e.g. `phase0/python/section1_identity.py`, `phase0/projects/weather_tool/`) even as empty stubs. Kacper wants to create each file himself and commit it one at a time as he actually does the work — see `docs/GIT_GUIDE.md`'s "never leave a session without committing" rule, which only makes sense if he's the one creating the files. `docs/REPO_STRUCTURE.md` is a reference for where things *should* eventually go, not something to build ahead of him. Docs (`docs/`, `phase0/README.md` as a checklist) are fine to create/edit — it's actual code files and folders under `phase0/`, `phase1/`, etc. that are his to create.

He's doing this for himself, not for anyone else — avoid superlatives or self-promotional framing about him (e.g. "ambitious," "excellent," "amazing exam result") anywhere in this repo's docs. He learns by digging into *why* something works rather than memorizing, and likes things tracked and structured — hence this whole restructuring effort. He's a 2nd-year Econometrics & Data Science student at University of Warsaw, not a CS/ML student, teaching himself this material outside his degree.

## Tutoring style — how Claude should actually work with him session-to-session
Confirmed directly by Kacper (2026-08-04):

- **When he's stuck:** point him at relevant resources (the specific book chapter, official docs, the right section of `docs/ROADMAP.md`'s resource lists) rather than giving hints or Socratic questioning. He wants to dig the answer out himself, not be walked to it.
- **Code review:** go line-by-line, everything — style, naming, edge cases, performance, idioms — not just correctness. Treat every review like a real, thorough PR review, not a quick pass.
- **Tests/validation:** depends on the project. Where `docs/phase0/projects.md` specifies explicit "done when" test criteria (e.g. Data Pipeline's 4 tests, NumPy Neural Net's `gradient_check` < 1e-4), Claude can write that check/test script for him. For drills and anything without a specified test, writing the test is part of the exercise — that's his to do, consistent with the no-vibecoding rule above.
- **Deadline pacing:** check in periodically against the Sept 27, 2026 Phase 0 target date and `phase0/README.md`'s checklist — proactively flag if he looks behind schedule rather than waiting to be asked. Don't be naggy about it; a rough check every so often, not every message.

## Exercise-authoring convention for future phase exercise files
Confirmed by Kacper (2026-08-04), after hitting this in Phase 0's `python_exercises.md`: Exercise 2.4's tasks C/D/E and Exercise 2.5's tasks C–F turned out to already contain fully-written, complete code in the exercise text itself — nothing actually left for him to write. That's a bug in how those exercises were authored (inherited from the original uploaded source material), not something Kacper is misreading — he flagged it correctly both times.

Rule for any exercise file Claude authors or edits going forward (Phase 1's `docs/phase1/python_exercises.md` etc., and if Kacper ever asks for a pass over Phase 0's remaining un-drilled sections): every numbered/lettered **task** within an exercise must leave something for Kacper to actually write — a blank (`...`), a `pass`-bodied function stub, an instruction like "write a function that does X" with no code shown, or similar. Do not give a task's complete working code in the exercise text itself; that turns "write this" into "read this," which is exactly what he doesn't want.

This doesn't apply to setup/scenario code that establishes shared context for the tasks that follow (e.g. Exercise 2.5's dataset-generation snippet, or Exercise 2.4's `numbers`/`words` lists) — that's fine to show in full, since it isn't itself one of the tasks. It also doesn't apply to short demo snippets used purely to illustrate a concept before the task list starts (e.g. showing what a generator expression looks like before asking him to write one). The distinguishing question for any given piece of code in an exercise: is this something the exercise is asking him to produce, or is it context he needs to do the actual asking? Only the former needs to stay incomplete.

**Second rule, confirmed by Kacper (2026-08-05):** exercises must not silently require tools or concepts that haven't been taught yet at that point in the curriculum. Hit this in Phase 0's `python_exercises.md` Exercise 3.5 Part B (`read_numbers`), which needs `open()`/file reading — that's Section 7 (File I/O) material, but the exercise sits in Section 3 (Functions in Depth). Same root cause as the first rule — inherited from the original uploaded source material, not something introduced by a Claude session, but Kacper doesn't want it repeated when authoring new phases' exercises from scratch.

Before including any task, check whether every function, module, or pattern it depends on has already been taught earlier — either earlier in the same document's own section order, or in an already-completed phase/section. If a task genuinely needs something not yet covered: reorder it to come after the section that teaches it, if that's practical; if reordering isn't practical (e.g. the concept genuinely belongs in a later section but this exercise is the first natural place to use it), say so explicitly in the exercise text and give the minimal syntax needed inline as a called-out preview, rather than silently assuming knowledge the reader doesn't have yet.

## Current state (as of 2026-08-04)
The doc restructuring AND the docs/phase0/ merge are both **done**. `phase0/` code scaffolding was deliberately **not** done — that's still Kacper's to create, see "Working style" above.

**Repo structure now:**
- `docs/ROADMAP.md`, `docs/GIT_GUIDE.md`, `docs/REPO_STRUCTURE.md` — course-wide planning docs, stay at `docs/` root.
- `docs/phase0/` — everything Phase-0-specific lives here, nothing Phase-0-specific stays at `docs/` root:
  - `README.md` — index: links, "how to structure your time," full Python/NumPy/Math completion checklist.
  - `python_concepts.md`, `numpy_concepts.md`, `math_concepts.md` — teaching content (read, don't drill).
  - `python_exercises.md`, `numpy_exercises.md` — ~70 Python + ~60 NumPy predict-before-run drills, plus Git/GitHub drills in the Python file's Section 8.
  - `habits_and_tools.md` — engineering/debugging/learning habits, editor setup.
  - `projects.md` — 4 core projects + 4 optional stretch, full specs. Renamed from `PHASE0_PROJECTS.md` and moved here from `docs/` root on 2026-08-04 at Kacper's request, for the same reason: it's Phase-0-scoped, so it belongs next to the rest of Phase 0's material, not alongside the course-wide docs. **If Phase 1+ ever get their own project-spec files, follow this same pattern** — `docs/phase1/projects.md`, not a `docs/PHASE1_PROJECTS.md` at root.
- `docs/MERGE_INSTRUCTIONS.md` is **deleted** — its checklist is fully done (see below).

**How the merge went (2026-08-04):** Kacper uploaded `phase0_complete.md`, `python_exercises.md`, `numpy_exercises.md`. Concepts (Parts 1–3 of `phase0_complete.md`) and drills (all sections of both exercise files) were split into the `docs/phase0/` files above, unchanged in substance. Cut during the merge, per `MERGE_INSTRUCTIONS.md` and Kacper's explicit request: `phase0_complete.md`'s Part 4 "Projects" section, and all project sections inside `python_exercises.md` (Config Manager, Data Pipeline, Mini ML Framework) and `numpy_exercises.md` (Data Preprocessing Engine, Gradient Descent Visualizer, NumPy Neural Network) — all superseded by `docs/phase0/projects.md`'s single canonical project list. `phase0_complete.md`'s §1.7 Git section and `python_exercises.md`'s Section 8 git-convention intro were replaced with pointers to `docs/GIT_GUIDE.md` (kept the hands-on §8.1–8.6 drills, just fixed the commit-message examples to the scoped convention). `ml_course_repo_structure.md` and `ml_engineer_roadmap.md` were never found anywhere (confirmed not needed — `REPO_STRUCTURE.md`/`ROADMAP.md` already fully replace them).

**Resolved:** the stale "full spec in the original..." pointers in `docs/phase0/projects.md`'s stretch section were removed at Kacper's request — the short specs there are enough to start; he'll ask for a fuller spec when he's actually ready to build a stretch project, rather than us maintaining dead references to deleted content.

**Confirmed:** Kacper wants Project 3 kept as the combined "Linear Regression from Scratch + Gradient Descent Visualizer" — no split needed. This is locked in.

**Also done (2026-08-04, same day, later session):** moved `docs/PHASE0_PROJECTS.md` → `docs/phase0/projects.md` at Kacper's request (see the `docs/phase0/` bullet above), and while touching cross-references, did a full staleness pass: fixed every reference to the old path across `CLAUDE.md`, `README.md`, `docs/ROADMAP.md`, `docs/phase0/README.md`, `docs/phase0/python_exercises.md`, `docs/phase0/numpy_exercises.md`, and `phase0/README.md`; rewrote `docs/REPO_STRUCTURE.md`'s directory diagram (it still showed `ROADMAP.md`/`GIT_GUIDE.md`/`PHASE0_PROJECTS.md` at the repo root from before the original `docs/` move, and its duplicate "README.md Template" + "requirements.txt" sections had already drifted from the real files — removed both duplicates in favor of pointing at the real files); removed two dead `MERGE_INSTRUCTIONS.md` references left in `docs/ROADMAP.md` from when that file was deleted; fixed a few bare `GIT_GUIDE.md` mentions that should've been `docs/GIT_GUIDE.md`. **Lesson for future sessions:** when a doc gets moved or deleted, grep the whole repo for its old filename before considering the job done — this is the second time stale cross-references slipped through.

## Conventions
- Commit messages: `type(scope): description` — see `docs/GIT_GUIDE.md` for the full convention and examples. Don't use the old unscoped style.
- Docs vs code split: `docs/` holds planning and instructional material (roadmap, project specs, concept explanations, exercise problem statements). Phase folders (`phase0/`, `phase1/`, ...) hold only code and a short status README. Don't let exercise prose creep back into the code folders.
- Phase 0 has a target date: **September 27, 2026**. If behind schedule, cut scope (drop a stretch project, skip exercises he's already comfortable with) rather than let the date slip.
