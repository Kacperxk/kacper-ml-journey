# ML Course Repository — Structure

Reference for where everything lives in this repo. `docs/` and each phase's
`README.md` already exist; the code subtrees inside each phase folder
(`phase0/python/`, `phase1/classical_ml/`, etc.) are targets — Kacper
creates those files himself as he works through each phase (see
`CLAUDE.md`'s working-style note; Claude should not pre-create them).

---

## Directory Structure

```
kacper-ml-journey/
│
├── README.md                          # master overview — your public face
├── CLAUDE.md                          # entry point for any Claude session in this repo
├── .gitignore                         # single gitignore for the whole repo (see docs/GIT_GUIDE.md)
├── requirements.txt                   # grows as you add libraries each phase
│
├── docs/                              # planning + instructional material
│   ├── ROADMAP.md                     # the 18-month, 6-phase roadmap
│   ├── GIT_GUIDE.md                   # canonical git workflow and commit convention
│   ├── REPO_STRUCTURE.md              # this file
│   └── phase0/                        # Phase 0 teaching content, drills, and project specs
│       ├── README.md                  # index: links, time structure, completion checklist
│       ├── python_concepts.md         # Python — OOP, functions, errors, types (read, don't drill)
│       ├── python_exercises.md        # ~70 Python drills + Git/GitHub drills
│       ├── numpy_concepts.md          # NumPy — arrays, broadcasting, linear algebra, einsum
│       ├── numpy_exercises.md         # ~60 NumPy drills
│       ├── math_concepts.md           # linear algebra, calculus, probability
│       ├── habits_and_tools.md        # engineering/debugging/learning habits, editor setup
│       └── projects.md                # 4 core projects + 4 optional stretch, full specs
│
├── phase0/                            # Foundations — target date Sept 27, 2026
│   ├── README.md                      # live status checklist (exists)
│   ├── python/                        # Kacper creates these as he works through python_exercises.md
│   │   ├── section1_identity.py
│   │   ├── section2_comprehensions.py
│   │   ├── section3_functions.py
│   │   ├── section4_oop.py
│   │   ├── section5_errors.py
│   │   ├── section6_typeHints.py
│   │   └── section7_fileIO.py
│   ├── numpy/                         # Kacper creates these as he works through numpy_exercises.md
│   │   │                               # .ipynb, not .py — numpy_exercises.md's own predict-before-run
│   │   │                               # methodology is meant to run in a notebook, one per section
│   │   ├── section1_creation.ipynb
│   │   ├── section2_indexing.ipynb
│   │   ├── section3_broadcasting.ipynb
│   │   ├── section4_aggregation.ipynb
│   │   ├── section5_linalg.ipynb
│   │   ├── section6_einsum.ipynb
│   │   ├── section7_numerical.ipynb
│   │   └── section8_ml_patterns.ipynb
│   └── projects/                      # docs/phase0/projects.md has the class/function-level spec
│       │                               # for each; each project's own README.md (written once
│       │                               # you build it) has its precise, as-built file structure
│       ├── weather_tool/              # Project 1 — CLI Weather Tool
│       ├── data_pipeline/             # Project 2 — Data Pipeline
│       ├── linear_regression/         # Project 3 — Linear Regression + GD Visualizer
│       ├── numpy_neural_net/          # Project 4 — capstone
│       └── stretch/                   # optional, only if ahead of schedule
│           ├── preprocessing_engine/
│           ├── config_manager/
│           ├── microtensor/
│           └── mini_ml/
│
├── phase1/                            # Classical ML
│   ├── README.md
│   ├── theory/
│   │   └── notes.md
│   ├── classical_ml/
│   │   ├── pandas_drills.py
│   │   ├── sklearn_pipelines.py
│   │   └── metrics_practice.py
│   └── projects/
│       └── ml_pipeline/
│           ├── eda.ipynb
│           ├── pipeline.py
│           ├── models.py
│           └── evaluate.py
│
├── phase2/                            # Deep Learning Core
│   ├── README.md
│   ├── backprop/
│   │   └── manual_backprop.py         # MLP from scratch
│   ├── cnn/
│   │   └── cifar10.py
│   ├── rnn/
│   │   └── char_lm.py
│   └── projects/
│       └── paper_reproduction/        # fill in once you pick a paper
│
├── phase3/                            # LLMs and Transformers (future)
│   └── README.md
│
├── phase4/                            # MLOps (future)
│   └── README.md
│
├── notebooks/                         # exploratory notebooks (not production)
│   └── python_scratchpad.ipynb
│
└── resources/                         # your notes, summaries, reading list
    ├── notes/                         # plain-language concept write-ups (see habits_and_tools.md)
    │   └── concept_name.md
    ├── paper_notes/
    │   └── attention_is_all_you_need.md
    └── reading_list.md
```

Note: Phase 5 ("Frontier Work & Portfolio") has no folder — it's ongoing, non-code work (papers, blog, open source), tracked via `resources/reading_list.md` and whatever blog/writing platform you pick, not a code phase.

`resources/` doesn't exist yet — create it once you have paper notes to put there, same "create it when you use it" rule as the phase folders.

---

## requirements.txt

Lives at the repo root, already populated for Phase 0 — see `requirements.txt` directly rather than duplicating its contents here. Add each later phase's packages when you actually reach that phase.

---

*Last updated: 2026-08-08*
