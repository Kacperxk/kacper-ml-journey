# Git Guide

The canonical git reference for this repo. Previously this content was duplicated (with two different, conflicting commit-message conventions) across the phase0 guide, the Python exercises doc, and the repo structure doc. This file replaces all three — the others should just link here.

---

## One-time setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Starting the repo (already done if you've pulled it to your Mac)

```bash
git clone https://github.com/Kacperxk/kacper-ml-journey.git
cd kacper-ml-journey
```

## Daily workflow

```bash
git status                              # what changed?
git diff                                # see the actual line changes
git add phase0/numpy/section3_broadcasting.ipynb   # stage a specific file
git add .                               # stage everything
git commit -m "feat(p0/numpy): implement pairwise distance without loops"
git push
```

## Commit message convention

Format: `<type>(<scope>): <description>`

- **type**: one of `feat`, `fix`, `refactor`, `test`, `docs`, `chore`
- **scope**: which phase/area — `p0/python`, `p0/numpy`, `p0/projects`, `p1/sklearn`, etc. Since every phase lives in one repo, the scope is what keeps `git log` readable.

```bash
git commit -m "feat(p0/numpy): implement pairwise distance without loops"
git commit -m "feat(p0/python): complete make_counter with nonlocal"
git commit -m "fix(p0/projects): correct gradient check in numpy neural net"
git commit -m "docs(p0): update phase 0 progress checklist"
git commit -m "chore: add matplotlib to requirements.txt"
```

This is the one convention to use everywhere — don't mix in the unscoped style from earlier drafts.

## Branching (use for every project, not for exercise drills)

```bash
git checkout -b project/linear-regression
# work, commit, work, commit...
git checkout main
git merge project/linear-regression
git branch -d project/linear-regression
git push origin --delete project/linear-regression   # if you pushed the branch
```

## Tagging milestones

```bash
# End of each exercise section
git tag -a p0-python-s1 -m "Phase 0: Python Section 1 complete"

# End of each project
git tag -a p0-project1-weather -m "Phase 0 Project 1: CLI Weather Tool complete"

# End of each phase
git tag -a phase0-complete -m "Phase 0 complete — Python, NumPy, math foundations"

git push --tags
```

## Useful history commands

```bash
git log --oneline --graph          # visual branch graph
git show HEAD                       # full diff of last commit
git diff HEAD~1 HEAD                # changes between last two commits
git blame phase0/python/section2_comprehensions.py   # who wrote each line (i.e. you, on which day)
# git blame on .ipynb files is a mess (raw JSON, output cells cause noise) — use it on .py files
git stash / git stash pop           # save work without committing
git revert HEAD                     # undo last commit safely (new commit, no history rewrite)
```

## `.gitignore` (single version for the whole repo)

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.venv/
venv/
env/
.env
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/

# Data — commit code that generates/downloads data, not the data itself
data/
*.csv
*.tsv
*.parquet
*.feather
*.h5
*.hdf5
*.json.gz

# Models — large binary files do not belong in git
checkpoints/
*.pt
*.pth
*.onnx
*.pkl
*.pickle
*.safetensors

# Outputs — generated, reproducible from code
outputs/
results/
logs/
*.log
figures/

# Secrets
.env
.env.*
*_key.json
credentials.json
secrets/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/settings.json
.idea/
```

## Rule for every exercise/project session

Never leave a session without committing something — even if it's just a note in a markdown file. Consistency beats intensity. If you've written 30+ minutes of code without committing, you're overdue.

---

*Last updated: 2026-08-04*
