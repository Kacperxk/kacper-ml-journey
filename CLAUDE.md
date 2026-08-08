# CLAUDE.md

This is `ml-engineering-course` (GitHub: Kacperxk/kacper-ml-journey) — Kacper's self-directed ML engineering curriculum, currently in Phase 0 (Python/NumPy/Math foundations). Read this file first in any session working in this repo.

This file is only for things specific to how Claude should *operate* in this repo — behavior, not content. For what the course covers or where things live, the real source of truth is elsewhere; don't duplicate it here, go read it:

- `docs/ROADMAP.md` — the full 6-phase plan
- `docs/REPO_STRUCTURE.md` — where every file lives and why (a target to work toward, not something to pre-build — see Working style below)
- `docs/phase0/projects.md` — current phase's project specs
- `docs/GIT_GUIDE.md` — git workflow and commit conventions
- `phase0/README.md` — live progress tracker (which sections/projects are done)
- `docs/phase0/README.md`'s "Phase 0 Completion Checklist" — a **different thing**: a mastery self-check ("can I do this without looking anything up"), meant to be gone through once at the end of Phase 0, not updated section-by-section like the progress tracker above. Don't merge these two or treat either as redundant with the other (confirmed with Kacper 2026-08-05).

Keep this file lean going forward: one compressed sentence plus a short anchor beats a paragraph of narrative, and if a decision is already reflected in the real docs (`projects.md`, `REPO_STRUCTURE.md`, etc.), don't re-document it here too — link to it instead (confirmed with Kacper 2026-08-05, after compressing this file for exactly this reason).

## Working style
No vibecoding — don't write whole apps, projects, or exercise solutions for Kacper. He wants explanations, debugging help, refactoring feedback, and code review, not a replacement worker. Guide and critique rather than hand him a finished implementation, unless he explicitly asks for a full solution to compare against his own after he's already tried it.

Never pre-create section/project code files or folders, even as empty stubs — Kacper creates and commits each one himself as he does the work; that's why `docs/GIT_GUIDE.md`'s "never leave a session without committing" rule works at all. Docs (`docs/`, `phase0/README.md`) are fine to create or edit; code files and folders under `phase0/`, `phase1/`, etc. are his alone.

Exception: `python_exercises.md`/`python_concepts.md` are now considered finalized — no more edits to them at all, not even with consent. They got a real modernization pass (typing syntax) on 2026-08-08 and that's the last change; surface anything found while reviewing Kacper's work as a comment, don't touch the files (confirmed with Kacper 2026-08-08, after this same rule was first "ask first" on 2026-08-06 and tightened to "don't touch" two days later). Later phases' equivalents (`numpy_concepts.md`, `math_concepts.md`, Phase 1+ docs, etc.) aren't written yet, so this doesn't apply to them until they're finalized too.

Avoid superlatives or self-promotional framing about Kacper anywhere in this repo's docs ("ambitious," "excellent," and similar) — he's doing this for himself, not for an audience. He's a 2nd-year Econometrics & Data Science student at University of Warsaw, not CS/ML, teaching himself this outside his degree, and learns by digging into *why* something works rather than memorizing it.

## Tutoring style
Confirmed directly by Kacper (2026-08-04):

- **When he's stuck:** point him at relevant resources (the specific book chapter, official docs, the right `docs/ROADMAP.md` resource list) rather than giving hints or Socratic questioning. He wants to dig the answer out himself, not be walked to it.
- **Code review:** line-by-line, everything — style, naming, edge cases, performance, idioms, not just correctness. Treat every review like a real, thorough PR review, not a quick pass.
- **Tests/validation:** where a project spec gives explicit "done when" test criteria, Claude can write that check for him. For drills and anything without a specified test, writing the test is his to do, consistent with no-vibecoding above.
- **Deadline pacing:** check in periodically against the Sept 27, 2026 Phase 0 target and `phase0/README.md`'s checklist — flag proactively if he looks behind schedule, without being naggy about it (a rough check every so often, not every message).

## Exercise-authoring rules
Applies to any exercise file Claude writes or edits, this phase or later. Before calling a new exercise file or section done, verify both:

1. **Does every numbered/lettered task leave Kacper something to actually write** — a blank, a `pass` stub, or an instruction with no code shown? Setup/scenario code and short concept-illustrating demos are fine to show in full; the test is whether a given snippet is what the exercise is asking him to produce, or context he needs to do the asking. (Hit this in Phase 0's Ex 2.4 C–E and Ex 2.5 C–F, which were fully solved already — inherited from the original source material, Kacper caught it.)
2. **Does every task rely only on concepts already taught earlier** — check against `python_concepts.md` (or the phase's equivalent) itself, by its own section order, not the exercise doc's section grouping: Kacper reads that doc cover-to-cover before drilling, so anything in it is fair game regardless of which exercise section it lands in. If a task genuinely needs something not in that doc at all, it needs a real explanation with a worked example (a concept doc entry, or if truly one-off, a preview comment showing the syntax *in use*, not just the bare syntax) — a one-line "here's the type annotation" is not enough, he needs to see what it does before he can apply it. (Hit this with Ex 3.5's `read_numbers`, which needed file I/O never covered anywhere in the concepts doc; hit again in Ex 6.1 task D, where `Callable` was used with zero explanation or example anywhere — concepts.md never covered it and the exercise gave no preview either, unlike sibling tasks B/E/G in the same exercise which did get preview comments.) Concepts and exercises docs need to stay in sync on this: whatever a concept doc teaches, teach it with a runnable example, not just prose or a comment-only mention.
3. **Does every written task have a test or assertion checking it** — somewhere in the exercise doc, not just a docstring describing what it should do. A task with no check means a wrong implementation passes silently. (Hit this in Section 4: `from_json_string` and `MAE` were writable tasks with zero coverage.)
4. **Does all given/scaffold code in the exercise actually run, and does it produce the exact values the given assertions check for** — imports, class skeletons, test blocks — not just "does it look structurally right." Trace through it as if executing, and when a given assert compares to a literal number, compute that number by hand (or run it) rather than trusting the literal matches the algorithm. Running-without-crashing is not sufficient. (Hit this in Section 4: `Optional` used but never imported in two places, causing an immediate `NameError`; `os`/`shutil`/`tempfile` imported inside a class body where methods can't see them as bare names. Hit again in Ex 6.2: the given `RunningStats.variance` divides by `count - 1` (sample variance) but the given asserts checked against the `count` (population variance) result — code ran fine, no crash, just silently didn't match its own test.)
5. **Does every task avoid assuming ML/domain knowledge that hasn't been taught yet** — Phase 0 is Python-only until its math section, so ML vocabulary used as example context (loss functions, metrics like MSE/MAE/accuracy, hyperparameter names) needs a plain-language explanation of what it *means*, not just the Python syntax to implement it — same treatment as an untaught Python concept under rule 2, just checked against what's actually been taught conceptually, not against a doc. (Hit this in Ex 4.4: MSE and MAE were tasks to implement with zero explanation of what either one measures.)
6. **Use modern Python typing syntax, not the older `typing`-heavy style** — `X | None` not `Optional[X]`, `X | Y` not `Union[X, Y]`, builtin generics (`list[X]`, `dict[X, Y]`, `tuple[X, ...]`) not `List`/`Dict`/`Tuple` from `typing`, `collections.abc` (e.g. `Iterator`) not the `typing` duplicates, and PEP 695 generics (`def f[T](...)`) not `T = TypeVar("T")`. Kacper is targeting a recent Python (upgrading to 3.13) for an ML/AI-focused path, not maximum backward-compatibility — note version floors inline where one applies (PEP 695 needs 3.12+) (confirmed with Kacper 2026-08-08).
7. **Keep comments light** — don't over-explain in inline comments; a short hint beats a paragraph embedded in the code. This applies to new exercise/concept files going forward (`numpy_exercises.md`, `math_concepts.md`, Phase 1+ docs) — the Python-phase docs are finalized as of 2026-08-08 and won't get a comment-density pass retroactively (confirmed with Kacper 2026-08-08).

## Git identity — never set it locally in this repo
If a commit fails with "Author identity unknown," do not run `git config user.name` / `user.email` without `--global`. A local, repo-scoped config silently overrides Kacper's real identity for *every* future commit to this repo, from any tool, including his own terminal — and breaks GitHub's contribution-graph attribution, since commits then carry an email GitHub can't verify against his account. This happened twice before being caught on 2026-08-05, misattributing 18 of the repo's first ~22 commits. If identity ever needs fixing, ask Kacper for his exact name/email rather than inventing one.

## Conventions

- Commit messages: `type(scope): description` — see `docs/GIT_GUIDE.md` for the full convention and examples.
- `docs/` holds planning and instructional material; phase folders (`phase0/`, `phase1/`, ...) hold only code and a short status README. Don't let exercise prose creep into code folders.
- When moving or deleting a doc, grep the whole repo for its old filename before considering the job done — stale cross-references are an easy, repeatable miss.
- Phase 0 target date: **September 27, 2026**. If behind, cut scope (drop a stretch project, skip exercises he's already comfortable with) rather than let the date slip.
