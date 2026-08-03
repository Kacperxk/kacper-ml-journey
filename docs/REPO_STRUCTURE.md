# ML Course Repository — Structure

Reference for where things go. The `docs/` and `phase0/README.md` layout
below already exists; the `phase0/python/`, `phase0/numpy/`, and
`phase0/projects/` subtrees are the target — Kacper creates those files
himself as he works through Phase 0 (see `CLAUDE.md`'s working-style note;
Claude should not pre-create them).

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
│       ├── python_concepts.md         # Part 1 — Python (read, don't drill)
│       ├── python_exercises.md        # ~70 Python drills + Git/GitHub drills
│       ├── numpy_concepts.md          # Part 2 — NumPy
│       ├── numpy_exercises.md         # ~60 NumPy drills
│       ├── math_concepts.md           # Part 3 — linear algebra, calculus, probability
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
│   │   ├── section6_types.py
│   │   └── section7_files.py
│   ├── numpy/                         # Kacper creates these as he works through numpy_exercises.md
│   │   ├── section1_creation.py
│   │   ├── section2_indexing.py
│   │   ├── section3_broadcasting.py
│   │   ├── section4_aggregation.py
│   │   ├── section5_linalg.py
│   │   ├── section6_einsum.py
│   │   ├── section7_numerical.py
│   │   └── section8_ml_patterns.py
│   └── projects/                      # see docs/phase0/projects.md for full specs
│       ├── weather_tool/              # Project 1 — CLI Weather Tool
│       │   ├── exceptions.py
│       │   ├── fetcher.py
│       │   ├── analyzer.py
│       │   └── cli.py
│       ├── data_pipeline/             # Project 2 — Data Pipeline
│       │   ├── sources.py
│       │   ├── transforms.py
│       │   ├── pipeline.py
│       │   └── sinks.py
│       ├── linear_regression/         # Project 3 — Linear Regression + GD Visualizer
│       │   ├── linear_regression.py
│       │   ├── optimizers.py          # vanilla GD, momentum, Adam
│       │   └── visualize.py
│       ├── numpy_neural_net/          # Project 4 — capstone
│       │   ├── network.py
│       │   ├── losses.py
│       │   └── gradient_check.py
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
│   ├── classical_ml/                  # renamed from sklearn_pandas — was mixing two library names
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
│   ├── phase0_numpy_exploration.ipynb
│   └── phase1_eda_titanic.ipynb
│
└── resources/                         # your notes, summaries, reading list
    ├── paper_notes/
    │   └── attention_is_all_you_need.md
    └── reading_list.md
```

Note: Phase 5 ("Frontier Work & Portfolio") has no folder — it's ongoing, non-code work (papers, blog, open source), tracked via `resources/reading_list.md` and whatever blog/writing platform you pick, not a code phase.

`notebooks/` and `resources/` don't exist yet either — create them if/when you actually have exploratory notebooks or paper notes to put there, same "create it when you use it" rule as the phase folders.

---

## requirements.txt

Lives at the repo root, already populated for Phase 0 — see `requirements.txt` directly rather than duplicating its contents here (that duplication is exactly the kind of drift this doc used to have). Add each later phase's packages when you actually reach that phase.

---

*Last updated: 2026-08-04*
