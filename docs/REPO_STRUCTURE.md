# ML Course Repository — Structure and README Template

Changes from the original: `sklearn_pandas/` renamed to `classical_ml/` (was mixing two library names), `phase0/projects/` now matches the 4 core projects in `PHASE0_PROJECTS.md` with a separate `stretch/` subfolder for the optional ones, and git setup content moved out to `GIT_GUIDE.md` instead of being embedded here.

---

## Directory Structure

```
ml-engineering-course/
│
├── README.md                          # master overview — your public face
├── ROADMAP.md                         # the 18-month roadmap
├── PHASE0_PROJECTS.md                 # Phase 0 project specs (core + stretch)
├── GIT_GUIDE.md                       # canonical git workflow and conventions
├── .gitignore                         # single gitignore for the whole repo (see GIT_GUIDE.md)
├── requirements.txt                   # grows as you add libraries each phase
│
├── phase0/                            # Foundations — target date Sept 27, 2026
│   ├── README.md                      # phase-specific notes and progress
│   ├── python/
│   │   ├── section1_identity.py
│   │   ├── section2_comprehensions.py
│   │   ├── section3_functions.py
│   │   ├── section4_oop.py
│   │   ├── section5_errors.py
│   │   ├── section6_types.py
│   │   └── section7_files.py
│   ├── numpy/
│   │   ├── section1_creation.py
│   │   ├── section2_indexing.py
│   │   ├── section3_broadcasting.py
│   │   ├── section4_aggregation.py
│   │   ├── section5_linalg.py
│   │   ├── section6_einsum.py
│   │   ├── section7_numerical.py
│   │   └── section8_ml_patterns.py
│   └── projects/                      # see PHASE0_PROJECTS.md for full specs
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
│   ├── classical_ml/                  # renamed from sklearn_pandas
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

---

## requirements.txt (grows with each phase)

```
# Phase 0
numpy>=1.26
matplotlib>=3.8
jupyter>=1.0

# Phase 1 (add when you reach it)
# pandas>=2.1
# scikit-learn>=1.4
# xgboost>=2.0
# lightgbm>=4.0
# seaborn>=0.13
# optuna>=3.5

# Phase 2 (add when you reach it)
# torch>=2.2
# torchvision>=0.17

# Dev
# pytest>=8.0
# black>=24.0
# ruff>=0.3
```

---

## README.md Template

```markdown
# ML Engineering Course

Self-directed study toward becoming an ML engineer. Structured as a 6-phase,
~18-month curriculum covering Python foundations through LLMs and alignment.

**Current phase:** Phase 0 — Python, NumPy, Math Foundations
**Phase 0 target date:** September 27, 2026
**Started:** [your start date]
**Target completion:** ~18 months from start

---

## The Goal

Working as an ML engineer on large-scale language models. The path there:
build genuine depth in every layer of the stack — from Python internals to
transformer training to alignment techniques.

See ROADMAP.md for the full plan, PHASE0_PROJECTS.md for current project specs,
and GIT_GUIDE.md for the workflow this repo follows.

---

## Structure

| Phase | Topic | Duration | Status |
|-------|-------|----------|--------|
| 0 | Python · NumPy · Math Foundations | target date Sept 27, 2026 | In progress |
| 1 | Classical ML · Scikit-learn | ~8 weeks | Not started |
| 2 | Deep Learning · Backprop · CNNs · RNNs | ~10 weeks | Not started |
| 3 | LLMs · Transformers · Attention | ~12 weeks | Not started |
| 4 | MLOps · Distributed Training · Inference | ~8 weeks | Not started |
| 5 | Frontier Work & Portfolio | ongoing | Not started |

---

## Phase 0 — Current Progress

**Python exercises** — see phase0/python/, ~70 exercises across 7 sections
**NumPy exercises** — see phase0/numpy/, ~60 exercises across 8 sections
**Projects** — see PHASE0_PROJECTS.md: 4 core (Weather Tool, Data Pipeline,
Linear Regression, NumPy Neural Network) + optional stretch

---

## Setup

\`\`\`bash
git clone https://github.com/YOURUSERNAME/ml-engineering-course.git
cd ml-engineering-course
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
\`\`\`

---

## Workflow

See GIT_GUIDE.md for commit conventions, branching, and tagging.

---

## Contact

[Your name] · [Your GitHub profile link]
```

---

*Last updated: 2026-08-03*
