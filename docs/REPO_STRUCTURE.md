# ML Course Repository — Structure

Reference for where everything lives in this repo. `docs/` and each phase's
`README.md` already exist; the code subtrees inside each phase folder
(`phase0/python/`, `phase0/numpy/`, etc.) are targets — Kacper creates
those files himself as he works through each phase (see `CLAUDE.md`'s
working-style note; Claude should not pre-create them).

---

## Directory Structure

```
kacper-ml-journey/
│
├── README.md                          # master overview — your public face
├── CLAUDE.md                          # entry point for any Claude session in this repo
├── .gitignore                         # single gitignore for the whole repo (see docs/GIT_GUIDE.md)
├── .python-version                    # pinned Python version
├── requirements.txt                   # grows as you add libraries each phase
│
├── docs/                              # planning + instructional material
│   ├── ROADMAP.md                     # the 18-month, 6-phase roadmap
│   ├── GIT_GUIDE.md                   # canonical git workflow and commit convention
│   ├── REPO_STRUCTURE.md              # this file
│   ├── mastery/                       # evidence-based depth tracking, separate from completion
│   │   └── phase0.md                  # one file per phase, populated as evidence accrues
│   ├── dsa/                           # Data Structures & Algorithms parallel track
│   │   └── README.md                  # path (book + NeetCode 150), method, progress
│   ├── phase1/                        # Phase 1 plan, reading guides, drills, specs
│   │   ├── README.md                  # modules, sections, resources, reading map, project outlines
│   │   ├── <module>_concepts.md       # per module: reading guide + notes (added when module starts)
│   │   ├── <module>_exercises.md      # per module: drills by section (added when module starts)
│   │   └── projects.md                # project specs (added before each project)
│   ├── audits/                        # dated, evidence-based periodic repo/curriculum reviews
│   │   └── YYYY-MM-DD-full-audit.md   # one file per audit
│   └── phase0/                        # Phase 0 teaching content, drills, and project specs
│       ├── README.md                  # index: links, time structure, completion checklist
│       ├── python_concepts.md         # Python — OOP, functions, errors, types (read, don't drill)
│       ├── python_exercises.md        # 24 Python drills (several multi-part) + Git/GitHub drills
│       ├── numpy_concepts.md          # NumPy — arrays, broadcasting, linear algebra, einsum
│       ├── numpy_exercises.md         # 36 NumPy drills (several multi-part)
│       ├── matplotlib_concepts.md     # figure/axes, plot types, subplots, saving
│       ├── math_concepts.md           # linear algebra, calculus, probability
│       ├── habits_and_tools.md        # engineering/debugging/learning habits, editor setup
│       ├── projects.md                # 4 core projects + stretch options (full spec: microtensor)
│       ├── linear_regression_project_explained.pdf     # Kacper's in-depth notes, Project 3
│       └── NumPy_Neural_Network_project_explained.pdf  # Kacper's in-depth notes, Project 4
│
├── phase0/                            # Foundations — complete, 2026-09-27
│   ├── README.md                      # live status checklist — section topics tracked here,
│   │                                   # not duplicated below
│   ├── python/                        # section1_*.py .. section7_*.py, one per section
│   ├── numpy/                         # section1_*.ipynb .. section8_*.ipynb — notebooks, not
│   │                                   # .py (numpy_exercises.md's predict-before-run methodology
│   │                                   # runs in a notebook)
│   └── projects/                      # docs/phase0/projects.md has the class/function-level spec
│       │                               # for each; each project's own README.md (written once
│       │                               # you build it) has its precise, as-built file structure
│       ├── weather_tool/              # Project 1 — CLI Weather Tool
│       ├── data_pipeline/             # Project 2 — Data Pipeline
│       ├── linear_regression/         # Project 3 — Linear Regression + GD Visualizer
│       ├── numpy_neural_net/          # Project 4 — capstone
│       └── microtensor/               # stretch — scalar autograd engine (the only stretch
│                                       # project built; the other 3 in projects.md weren't)
│
├── phase1/                            # Classical ML — target date Nov 29, 2026
│   ├── README.md                      # live status checklist
│   ├── pandas/                        # section1_*.ipynb .. section8_*.ipynb
│   ├── stats/                         # section1_*.ipynb .. section4_*.ipynb
│   ├── evaluation/                    # section1_*.ipynb .. section5_*.ipynb
│   ├── linear_models/                 # section1_*.ipynb .. section4_*.ipynb
│   ├── trees/                         # section1_*.ipynb .. section4_*.ipynb
│   ├── other_methods/                 # section1_*.ipynb .. section5_*.ipynb
│   └── projects/                      # data project, from-scratch models, capstone
│
├── dsa/                               # DSA track solutions: <NN>-<block>/<problem_slug>.py
│                                       # (see docs/dsa/README.md)
│
├── phase2/                            # Deep Learning Core — structure TBD, expand once you start
│   └── README.md                      # see docs/ROADMAP.md Phase 2 for topics/projects
│
├── phase3/                            # LLMs and Transformers (future)
│   └── README.md
│
├── phase4/                            # MLOps (future)
│   └── README.md
│
├── notebooks/                         # exploratory notebooks (not production)
│   ├── python_scratchpad.ipynb
│   └── matplotlib_practice.ipynb
│
└── resources/                         # your notes, summaries, reading list
    ├── paper_notes/
    │   └── attention_is_all_you_need.md
    └── reading_list.md
```

Note: Phase 5 ("Frontier Work & Portfolio") has no folder — it's ongoing, non-code work (papers, blog, open source), tracked via `resources/reading_list.md` and whatever blog/writing platform you pick, not a code phase.

`resources/` doesn't exist yet — create it once you have paper notes to put there, same "create it when you use it" rule as the phase folders.

---

## requirements.txt

Lives at the repo root, already populated for Phases 0 and 1 — see `requirements.txt` directly rather than duplicating its contents here. Add each later phase's packages when you actually reach that phase.

---

*Last updated: 2026-09-30*
