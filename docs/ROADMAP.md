# ML Engineer Roadmap
### For: Econometrics & Data Science student, University of Warsaw | 3–4 hrs/day | ~18 months

---

> **How to use this document:** This is a living reference. Every phase has a goal, a skill checklist, concrete resources, and projects to prove you learned it. Come back here often. When you finish a phase, expand the next one in more detail.
>
> **v2 note:** This revises the original roadmap. Changes: removed a reference to an unverified/likely-fictional Anthropic model name ("Mythos") — don't build career narrative on facts that might not be real; added a target date for Phase 0 instead of an open-ended one; moved the Phase 0 project list out of this document into `PHASE0_PROJECTS.md` (the old version had three different, non-overlapping project lists scattered across three files — see `MERGE_INSTRUCTIONS.md` for the full explanation).

---

## Starting Profile

**Background going in:**
- Math foundation from econometrics coursework (linear algebra, calculus, probability/stats)
- Python basics — can write scripts, understands control flow
- Exposure to data concepts from your degree
- C1 English — can read papers, docs, courses without friction

**Gaps to close before ML work gets serious:**
- Python needs to reach "fluent" level (OOP, clean code, tooling)
- NumPy needs to be second nature
- ML library stack (PyTorch above all) is essentially untouched
- No experience yet with model training pipelines, distributed systems, or deployment

**The honest timeline:** 18 months at 3–4 hrs/day is achievable to reach junior/mid ML Engineer level competitive for roles at serious AI labs — but only if you are consistent and project-driven, and only if each phase has a real deadline. Open-ended phases expand to fill the time available; that's what happened to the original Phase 0 plan (see below).

---

## The Big Picture — All 6 Phases

```
Phase 0 │ Foundations Refresh         │ ~8 weeks (see below)
Phase 1 │ ML Theory + Classical ML    │ ~8 weeks
Phase 2 │ Deep Learning Core          │ ~10 weeks
Phase 3 │ LLMs & Transformers         │ ~12 weeks
Phase 4 │ MLOps & Systems             │ ~8 weeks
Phase 5 │ Frontier Work & Portfolio   │ ongoing
```

These phases overlap in practice. Don't treat them as strict sequential blocks — once you start Phase 2, you keep coding Python. Once you start Phase 3, you keep reading papers.

---

## PHASE 0 — Foundations Refresh
### Target date: **September 27, 2026** (~8 weeks from Aug 3, 2026) | Goal: Arrive at Phase 1 with zero weak spots holding you back

This date is fixed, not aspirational. University restarts in October and your daily hours drop — Phase 0 needs to be behind you before then. If you're not done by the target date, **cut remaining scope** (drop a stretch project, skip an exercise section you're already comfortable with) rather than slip the date. An unfinished Phase 0 that ends on time beats a "complete" one that eats into semester 3.

The goal here isn't to master everything — it's to remove blockers. You have the math. You have basic Python. This phase upgrades both to the level required for serious ML work.

### What's in Phase 0
- **Concepts**: Python (OOP, functions, error handling, types, project structure, git) + NumPy (arrays, indexing, broadcasting, linear algebra, einsum) + Math (linear algebra, calculus/backprop intuition, probability). Full teaching content — keep as-is from your existing `phase0/README.md`-equivalent notes.
- **Drills**: ~60 NumPy exercises, ~70 Python exercises. Keep as-is — these are genuinely well-built (predict-before-run methodology is worth keeping exactly as written).
- **Projects**: see `PHASE0_PROJECTS.md` — **4 core projects only**, not 9. The original plan had three separate, uncoordinated project lists (one per source document) totaling 9 projects, of which only 3 were ever wired into the actual repo structure. That's fixed now.
- **Git**: see `GIT_GUIDE.md` — one canonical workflow and commit convention, not three slightly different ones.

### 0A — Python: From Mediocre to Fluent

You need Python to feel like a natural extension of your thoughts, not something you have to fight. The ML Engineer stack is almost entirely Python.

**What to focus on:**
- **OOP properly** — classes, inheritance, dunder methods (`__init__`, `__repr__`, `__len__`), decorators (`@property`, `@staticmethod`, `@classmethod`). ML codebases use these constantly.
- **Pythonic idioms** — list/dict/generator comprehensions, `zip`, `enumerate`, `*args/**kwargs`, context managers (`with`), f-strings
- **Error handling** — `try/except`, custom exceptions, logging (not `print`)
- **Modules and packages** — how imports work, how to structure a project with `__init__.py`, relative vs absolute imports
- **Type hints** — `def train(model: nn.Module, lr: float) -> dict:` — standard in modern ML code
- **Virtual environments** — `venv` or `conda`, `requirements.txt`, `pyproject.toml`
- **Git basics** — see `GIT_GUIDE.md`. Non-negotiable for any engineering role.

**Resources:**
- *Fluent Python* by Luciano Ramalho — the definitive book. Read chapters 1–9 now, rest later.
- Real Python (realpython.com) — excellent free articles on specific topics
- For Git: *Pro Git* book (free at git-scm.com) chapters 1–3

### 0B — NumPy: Make It Second Nature

NumPy is the backbone of everything in ML. PyTorch tensors are conceptually the same as NumPy arrays. If NumPy feels unfamiliar, PyTorch will feel twice as hard.

**What to master:**
- Array creation, indexing/slicing (including boolean indexing)
- **Broadcasting** — the concept most people underestimate. Understand it deeply.
- Vectorized operations — never write a Python loop where NumPy can do it
- Linear algebra ops: `np.dot`, `@`, `np.linalg.inv`, `np.linalg.eig`, `np.linalg.svd`
- Shape manipulation: `reshape`, `transpose`, `squeeze`, `expand_dims`, `stack`, `concatenate`
- Reduction ops: `sum`, `mean`, `std`, `max`, `argmax` along specific axes

**Resources:**
- The official NumPy "Absolute Beginner's Guide" + "NumPy for Beginners" on numpy.org
- *Python for Data Analysis* by Wes McKinney
- CS231n's Python/NumPy tutorial (cs231n.github.io/python-numpy-tutorial)

### 0C — Math: Confirm and Fill Gaps

Your econometrics background covers some of this already. Run through this checklist — be honest about weak spots:

**Linear Algebra (critical — highest priority in all of ML):** matrix multiplication/transpose/inverse, dot products and cosine similarity, eigenvalues/eigenvectors, SVD, vector spaces/basis/rank/null space, norms (L1, L2, Frobenius).

**Calculus (for backpropagation):** partial derivatives and the gradient, chain rule (this IS backprop), Jacobians/Hessians (conceptual), Taylor series.

**Probability & Statistics (your econometrics gives you most of this):** distributions (Gaussian, Bernoulli, Categorical, softmax-as-distribution), MLE, Bayes' theorem, expectation/variance/covariance, KL divergence and cross-entropy as loss functions.

**Resources (fill gaps only):**
- *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong — free PDF at mml-book.github.io
- 3Blue1Brown's "Essence of Linear Algebra" — YouTube
- Gilbert Strang's MIT OCW Linear Algebra — if you want the rigorous treatment

---

## PHASE 1 — ML Theory + Classical ML
### Duration: ~8 weeks | Goal: Understand how ML works at the algorithmic level

### 1A — Core ML Concepts
Bias-variance tradeoff, train/val/test splits, cross-validation, loss functions (MSE, MAE, Cross-Entropy), optimization (GD/SGD/mini-batch), learning rate, regularization (L1/L2/dropout — connects to what you know from econometrics), evaluation metrics (accuracy, precision, recall, F1, ROC-AUC), feature engineering and scaling.

**Resources:** *Hands-On Machine Learning* by Aurélien Géron (3rd ed.), chapters 1–9. StatQuest with Josh Starmer on YouTube.

### 1B — Classical Algorithms (Scikit-learn)
Linear/Logistic Regression, Decision Trees, Random Forests, Gradient Boosting (XGBoost/LightGBM), k-NN, SVMs, k-Means, PCA.

**Resources:** *Hands-On ML* chapters 4–7. Scikit-learn User Guide. Kaggle Learn.

**Project for Phase 1:** Pick a real Kaggle dataset (Titanic, House Prices, or similar). Build a complete pipeline: EDA, feature engineering, 3+ models, hyperparameter tuning, proper held-out evaluation. Write it up in a notebook, push to GitHub. First portfolio piece.

---

## PHASE 2 — Deep Learning Core
### Duration: ~10 weeks | Goal: Train neural networks confidently in PyTorch

### 2A — Neural Networks from First Principles
The neuron, layers and depth, activation functions (ReLU, GELU), forward pass, backprop (mathematically), weight initialization (Xavier/Kaiming), batch norm, dropout.

**Resources:** Andrej Karpathy's "Neural Networks: Zero to Hero" (the single best resource — watch all of it). *Deep Learning* by Goodfellow et al., chapters 6–9 (free at deeplearningbook.org). 3Blue1Brown "Neural Networks" series.

### 2B — PyTorch
Tensors, `torch.autograd`, `nn.Module`, core layers, loss functions, optimizers, the training loop (`zero_grad → forward → loss → backward → step`), `DataLoader`/`Dataset`, GPU usage, saving/loading models.

**Resources:** Official PyTorch tutorials ("Learn the Basics"). Karpathy's micrograd and makemore repos.

**Projects for Phase 2:**
1. MLP from scratch in pure NumPy/Python (Karpathy's micrograd project) — non-negotiable.
2. CNN image classifier on CIFAR-10 in PyTorch, full custom training loop.
3. Reproduce a small paper (LeNet, a simple RNN LM, or a basic VAE).

### 2C — Important Architectures
CNNs (convolution, pooling, ResNet), RNNs/LSTMs (vanishing gradients), autoencoders/VAEs, embeddings.

---

## PHASE 3 — LLMs & Transformers
### Duration: ~12 weeks | Goal: Deeply understand how frontier language models are built

### 3A — The Transformer Architecture
Read *"Attention Is All You Need"* (Vaswani et al., 2017) — twice, once before and once after the concepts below. Tokenization (BPE, SentencePiece), embeddings + positional encoding, self-attention (`softmax(QKᵀ/√d_k)V`), causal masking, multi-head attention, feed-forward layers, layer norm, residual connections, encoder vs decoder blocks, scaling laws (Chinchilla).

**Resources:** Karpathy's "Let's build GPT from scratch" (mandatory). *The Illustrated Transformer* by Jay Alammar. Sebastian Raschka's LLM writeups. Research blogs from major AI labs (Anthropic, OpenAI, DeepMind, etc.).

### 3B — Training Language Models
Pre-training (next-token prediction, data curation, gradient accumulation, mixed precision, distributed training basics — DDP, model/pipeline/tensor parallelism, ZeRO), fine-tuning (SFT, RLHF, Constitutional AI-style techniques, RLAIF, LoRA/QLoRA, DPO).

**Resources:** Hugging Face course. LoRA paper (arxiv 2106.09685). DPO, Chinchilla papers.

### 3C — Key Ecosystem Tools
Hugging Face Transformers/Datasets, PEFT, TRL, vLLM, LangChain/LlamaIndex (know what they do, don't obsess).

**Projects for Phase 3:**
1. Build a GPT from scratch (Karpathy's nanoGPT, character-level) — non-negotiable.
2. Fine-tune an open-source LLM (7B class) with LoRA via Hugging Face + PEFT.
3. Implement a toy RLHF pipeline — minimal reward model, scoring, simplified preference optimization.

---

## PHASE 4 — MLOps & Systems
### Duration: ~8 weeks | Goal: Build, deploy, and monitor models like an engineer — not just a researcher

### 4A — Software Engineering Foundations for ML
Config management, testing (`pytest`), experiment tracking (wandb/MLflow), Docker, profiling/debugging.

### 4B — Compute and Scaling
GPU fundamentals, mixed precision (FP16/BF16), gradient checkpointing, Flash Attention (conceptual), quantization (INT8/INT4/GGUF), cloud compute basics.

### 4C — Evaluation and Safety
Eval frameworks (LM Eval Harness), benchmark literacy (MMLU, HumanEval, SWE-bench, GPQA, MATH), red-teaming, hallucination/calibration, bias/fairness evaluation, model/system cards.

### 4D — Deployment
Inference optimization (vLLM, TensorRT-LLM, ONNX), REST APIs (FastAPI), batch inference, model versioning.

**Project for Phase 4:** Deploy your fine-tuned LLM from Phase 3 as a REST API (FastAPI + vLLM), containerized with Docker, with wandb tracking and at least some unit tests. Full GitHub README.

---

## PHASE 5 — Frontier Work & Portfolio
### Duration: Ongoing from month ~15

### 5A — Reading Research Papers
How to read a paper (abstract/conclusion → figures → intro → methods → experiments). Build a reading list over time covering architecture foundations, training techniques, efficiency/systems, and alignment/safety — pull from arxiv.org, Papers With Code, and lab research blogs as you go, rather than committing to a fixed list now (avoids baking in facts that may be wrong or outdated).

### 5B — Open Source Contributions
Start small (docs, examples, tests) in a major ML repo (e.g. Hugging Face Transformers). Graduate to implementing a paper or improving a training script.

### 5C — Portfolio Strategy
Tier 1 (Phases 0–2): from-scratch implementations, classical ML pipeline, CNN classifier.
Tier 2 (Phase 3): GPT from scratch, fine-tuned LLM with LoRA, toy RLHF/DPO.
Tier 3 (Phase 4): deployed model API, experiment tracking, distributed training or quantization work.
Tier 4 (Phase 5): paper reproduction with your own analysis, an original experiment, a write-up explaining something you learned deeply.

**Blog:** Write about what you learn — for clarity, not marketing. If you can explain self-attention from first principles in writing, you understand it.

### 5D — Staying Current
Follow major lab research blogs, Hugging Face Blog, Karpathy, Sebastian Raschka's newsletter, and similar. Weekly habit: 30 minutes skimming arxiv abstracts (cs.LG, cs.CL) on Fridays, read one paper properly per week.

---

## Parallel Tracks (Run Alongside Everything)

**Leetcode / DSA:** 2–3 problems/week, consistently. Focus: arrays, hashmaps, trees, graphs, DP, recursion. Resource: Neetcode.io.

**Linear Algebra Deepening:** eigendecomposition in the context of PCA, SVD in the context of LoRA, optimization theory.

**English Technical Writing:** commit messages, docstrings, READMEs, eventually paper/technique explanations.

---

## Recommended Full Resource Stack (Prioritized)

**Books:** *Mathematics for Machine Learning* (free PDF), *Hands-On Machine Learning* (Géron), *Deep Learning* (Goodfellow, free PDF), *Fluent Python* (Ramalho).

**Video courses:** Karpathy "Neural Networks: Zero to Hero", Fast.ai "Practical Deep Learning", Hugging Face Course, CS231n Stanford, DeepLearning.AI short courses.

**Practice platforms:** Kaggle, Hugging Face Hub, Google Colab / Kaggle Notebooks (free GPU).

---

## Month-by-Month Suggested Schedule

| Month | Primary Focus | Side Track |
|-------|--------------|------------|
| 1 | Phase 0 (target date Sept 27) | Git, CLI tools |
| 2 | Phase 1: classical ML + first Kaggle project | Leetcode starts |
| 3 | Phase 2: neural nets from scratch + backprop | Read first papers |
| 4 | Phase 2: PyTorch core + CNN project | Fast.ai |
| 5 | Phase 2: architectures, wrap up | Reproduce a paper |
| 6 | Phase 3: Transformers + Attention | Attention paper |
| 7 | Phase 3: Build GPT from scratch | Read BERT, GPT-2 |
| 8 | Phase 3: Hugging Face ecosystem + fine-tuning | LoRA paper |
| 9 | Phase 3: RLHF-style training, DPO | Alignment papers |
| 10 | Phase 3 wrap: LoRA fine-tuning project | Open model papers |
| 11 | Phase 4: MLOps — Docker, wandb, tracking | Flash Attention |
| 12 | Phase 4: Deployment — FastAPI, vLLM | Open source contribution |
| 13 | Phase 4: distributed training concepts | DeepSpeed docs |
| 14 | Phase 4 wrap: evaluation, red-teaming, safety | System cards |
| 15 | Phase 5: original research experiment | Paper writing |
| 16 | Phase 5: portfolio polish, applications | Interview prep |
| 17–18 | Interview rounds, networking, open source | Stay current |

Note: months 2–14 will compress against university semester load — this schedule assumes ~3–4 hrs/day holds through the year. Revisit and adjust once you know your actual semester workload in October.

---

## Interview Preparation (Start Month 14–15)

**ML Engineer interviews typically have:**
1. Coding round — Leetcode medium, clean Python
2. ML theory round — explain backprop, attention, bias-variance, regularization from first principles
3. System design round — "design a training pipeline for a large model," "how would you serve an LLM at scale"
4. ML coding round — implement attention from scratch, write a training loop, debug a broken model
5. Research discussion — at frontier labs, expect discussion of recent papers and your own projects

---

## Honest Warnings

**Things that will derail you:**
- Tutorial hell — after every resource, build something.
- Switching frameworks constantly — pick PyTorch and go deep.
- Over-optimizing the roadmap instead of executing it — this document is a reference, not a comfort blanket.
- Skipping the math — it catches up with you when you need to debug or innovate.
- Only doing guided projects — eventually build something *you* defined, no tutorial holding your hand.
- **Letting phases run open-ended.** This is what happened to the original Phase 0 plan. Every phase needs a real deadline.

**Things that will accelerate you:**
- Finding a community (r/MachineLearning, Hugging Face Discord, ML Twitter/X)
- Working on something you're genuinely curious about
- Reading code of people you respect (Karpathy's repos)
- Explaining concepts to others — write, teach, discuss

---

## How We'll Use This Document

This roadmap is your anchor. When we talk again, we can:
- Deep-dive into any specific topic from any phase
- Build out detailed week-by-week schedules for a specific phase
- Review your project work and give feedback
- Discuss specific papers together
- Adjust the plan based on how you're progressing — and set a new target date for the next phase before it starts, the same way Phase 0 now has one

---

*Last updated: 2026-08-04 | Version 2.0 — consolidated from four previously-inconsistent source documents; see MERGE_INSTRUCTIONS.md*
