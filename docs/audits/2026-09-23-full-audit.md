# Full Repository Audit — 2026-09-23

Third weekly audit, since 2026-09-11. Scope: all of Project 4's build, the git-identity incident and its fix, a machine-divergence incident and its fix, and a fresh check of every doc, `.gitignore`, tags, and file structure — same standing checklist as the prior two audits.

## A. What changed since the last audit

Project 4 (NumPy Neural Network) went from "not started" to fully complete: `layers.py` (relu/relu_backward/softmax/cross_entropy), a `TwoLayerNet` with a hand-derived backward pass verified by its own `gradient_check` (~1e-9 relative error, well under the spec's 1e-4 bar), a mini-batch SGD training loop, training-curve plots, and a synthetic-data pipeline landing at 83% validation accuracy. All four Phase 0 core projects are now checked off in `phase0/README.md`, tagged (`p0-project4-numpy-neural-net`), and `docs/mastery/phase0.md` has a full evidence entry for the project, including that backprop genuinely didn't land on the first explanation and needed an external-resource detour (3Blue1Brown, Karpathy) before it did — recorded honestly rather than smoothed over.

## B. Problems found

**Git identity misattribution — the significant one this cycle, already fixed.** Starting from `d2d434f` (a Project 3 commit on 2026-09-09), I began committing under the wrong identity (`Kacperxk <kacbad2005@gmail.com>`) instead of the repo's actual configured identity (`Kacper <kacperbadowicz8@gmail.com>`) — an email I pulled from my own conversation context instead of checking `git config` or prior commit history first. 13 commits were affected. Investigating this also surfaced that the *original* incident `CLAUDE.md` already documents — "misattributed 18 of the first ~22 commits (caught 2026-08-05)" — had never actually been corrected. "Caught" in that note meant the practice stopped going forward; the 18 already-bad commits were left wrong on GitHub for over six weeks. Combined: 31 commits, roughly a fifth of the repo's history, silently unlinked from Kacper's GitHub profile since early August. Found only because Kacper noticed his contribution graph looked wrong and asked. Fixed via `git filter-branch --env-filter` rewriting all 31 commits' author and committer identity, then a force-push (explicitly confirmed with Kacper first, given it rewrites already-public history). Also found and removed a duplicate Project 3 tag (`p0-project3-linearregression`) that existed alongside the correctly-named one, created directly by Kacper around the same time, apparently without either of us noticing the other's tag.

The real process failure here isn't the original mistake — it's that the 2026-08-05 audit recorded the incident as resolved without verifying the actual bad commits got corrected, and I then repeated the identical bug independently five weeks later without checking established convention first. Going forward: before using `-c user.name=/-c user.email=` on any commit, check `git log` or `git config --global` for the established identity rather than assuming context-provided contact info is the same thing as a git identity. When an audit records an incident as "resolved," that should mean the artifacts are actually fixed, not just that a rule was written down.

**Machine divergence — minor, already fixed.** A commit made directly from Kacper's PC (adding a PDF to `docs/`) was pushed to `origin/main` while this session's local checkout, running on a different machine, kept building Project 4 without pulling it first. Local and remote diverged (5 commits ahead locally, 1 ahead on origin). No actual conflict — different files entirely — so a clean `git pull --rebase`-equivalent resolved it with zero conflicts. Added one line to `GIT_GUIDE.md`'s Daily Workflow section recommending a `git pull` at the start of a session when switching machines, to avoid this recurring.

**Everything else checked, nothing else found.** File structure under `phase0/projects/numpy_neural_net/` matches `REPO_STRUCTURE.md`'s target exactly. No ignored files (`__pycache__/`, `.pytest_cache/`, `figures/`) leaked into tracked history. Every doc's footer date is consistent with its actual last change. `requirements.txt` needed no additions for Project 4 (numpy/matplotlib already covered). All 159 commits now share one consistent, correct author identity. Working tree clean.

## C. Deliberately not changed

Root `README.md`'s phase-status table still lists Phase 0 as "In progress," even though all four core projects are done. Left as-is on purpose: `docs/phase0/README.md`'s "Phase 0 Completion Checklist" is the actual gate for calling the phase done (an honest self-assessment, separate from project completion per `CLAUDE.md`'s own architecture), and the stretch-project decision is still open. Both are Kacper's calls to make, not something this audit should preempt.

## D. No action needed beyond B

Nothing in `ROADMAP.md`, `REPO_STRUCTURE.md`, `docs/phase0/README.md`, or `docs/phase0/projects.md` has drifted from actual repo state this cycle.

---

*Audit conducted and resolved: 2026-09-23*
