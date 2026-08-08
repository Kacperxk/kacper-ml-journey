# CLAUDE.md

`ml-engineering-course` (GitHub: Kacperxk/kacper-ml-journey) — Kacper's self-directed ML engineering curriculum, currently Phase 0 (Python/NumPy/Math foundations). Read this file first in any session in this repo.

This file covers only how Claude should *operate* here — not course content. Source of truth for content:

- `docs/ROADMAP.md` — full 6-phase plan
- `docs/REPO_STRUCTURE.md` — file layout (a target, not pre-built — see Working style)
- `docs/phase0/projects.md` — current phase's project specs
- `docs/GIT_GUIDE.md` — git workflow and commit conventions
- `phase0/README.md` — live progress tracker (sections/projects done)
- `docs/phase0/README.md`'s "Phase 0 Completion Checklist" — separate thing: a one-time end-of-phase mastery self-check, not a section-by-section tracker. Don't merge with the above (2026-08-05).

Keep this file lean: one compressed sentence + anchor beats a paragraph. If a decision already lives in `projects.md`/`REPO_STRUCTURE.md`/etc., link to it, don't duplicate it.

## Working style

No vibecoding — no whole apps/projects/exercise solutions for Kacper. Explanations, debugging help, refactoring feedback, code review only. Full solutions only if he explicitly asks, after he's already tried it himself.

Never pre-create section/project code files or folders, even as stubs — Kacper creates and commits each one himself (this is what makes `docs/GIT_GUIDE.md`'s "never leave a session without committing" rule work). Docs (`docs/`, `phase0/README.md`) are Claude's to create/edit; code under `phase0/`, `phase1/`, etc. is Kacper's alone.

No superlatives or self-promotional framing about Kacper anywhere in this repo's docs ("ambitious," "excellent," etc.) — this is for himself, not an audience. 2nd-year Econometrics & Data Science student (Warsaw), not CS/ML, self-taught outside his degree, learns by digging into *why*.

## Tutoring style

Confirmed 2026-08-04:

- **Stuck:** point to resources (book chapter, official docs, `docs/ROADMAP.md`'s list) — not hints or Socratic questioning. He digs out the answer himself.
- **Code review:** line-by-line — style, naming, edge cases, performance, idioms. Real PR-review depth, not a quick pass.
- **Tests:** projects with explicit "done when" criteria — Claude can write the check. Drills without a specified test — his to write.
- **Deadline pacing:** check against the Sept 27, 2026 target / `phase0/README.md` checklist periodically. Flag if behind, without being naggy about it.

## Exercise-authoring rules

Applies to any exercise file Claude writes or edits, this phase or later. Before marking a file/section done, verify:

1. **Every task leaves something to write** — a blank, a `pass` stub, or a code-free instruction. Setup/demo code can be shown in full. (Ex 2.4 C–E, 2.5 C–F: fully solved already, inherited from source material.)
2. **Every task relies only on concepts already taught** — checked against the concepts doc's own section order, not the exercise doc's. Anything genuinely new needs a real explanation + worked example, not a bare syntax mention. (Ex 3.5 `read_numbers`: file I/O never covered. Ex 6.1 task D: `Callable` used with zero explanation, unlike sibling tasks B/E/G.)
3. **Every written task has a test/assertion** — not just a docstring. (Section 4: `from_json_string`, `MAE` had zero coverage.)
4. **Given/scaffold code runs and matches its own asserts' literal values** — hand-compute, don't trust the literal. (Section 4: `Optional` unimported → `NameError`. Ex 6.2: `RunningStats.variance` used sample variance, asserts expected population variance — ran fine, silently wrong.)
5. **No untaught ML/domain knowledge assumed** — Phase 0 is Python-only until its math section; ML terms (loss functions, MSE/MAE/accuracy) need plain-language explanation, same treatment as an untaught Python concept. (Ex 4.4: MSE/MAE implemented with zero explanation of what either measures.)
6. **Modern Python typing** — `X | None` not `Optional[X]`, `X | Y` not `Union[X, Y]`, builtin generics not `List`/`Dict`/`Tuple`, `collections.abc` not `typing` duplicates, PEP 695 `def f[T](...)` not `TypeVar`. Targeting Python 3.13; note version floors inline (PEP 695 needs 3.12+).
7. **Light comments** — a short hint beats a paragraph embedded in code. Applies to new files going forward (`numpy_exercises.md`, `math_concepts.md`, Phase 1+); no retroactive comment-density pass on `python_concepts.md`/`python_exercises.md` unless asked.

## Git identity — never set it locally in this repo

If a commit fails with "Author identity unknown," never run `git config user.name`/`user.email` without `--global` — a local config silently overrides Kacper's identity for every future commit from any tool, and breaks GitHub attribution. Happened twice, misattributed 18 of the first ~22 commits (caught 2026-08-05). If identity ever needs fixing, ask Kacper for his exact name/email.

## Conventions

- Minimal prose in every `.md` file, this one included — state the fact, stop. No parenthetical justification or narrated reasoning; that goes in chat instead. (A `Time: ~10-14 hours` line in `projects.md` got padded with a justification + calendar-math footnote — zero added value; 2026-08-08.)
- Commit messages: `type(scope): description` — see `docs/GIT_GUIDE.md`.
- `docs/` = planning/instructional material. Phase folders (`phase0/`, `phase1/`, ...) = code + short status README only. No exercise prose in code folders.
- Moving/deleting a doc: grep the whole repo for the old filename first — stale cross-references are an easy, repeatable miss.
- Phase 0 target: **September 27, 2026**. If behind, cut scope (drop a stretch project, skip comfortable exercises) rather than let the date slip.
