# ML Engineer Roadmap
### 3–4 hrs/day | ~18 months

---

> **How to use this document:** A living reference. Every phase has a goal, a skill checklist, concrete resources, and projects to prove you learned it. Before expanding the next phase, check its plan against current tools and practices first — content written this far ahead will drift, so verify before trusting it, then expand in more detail.

---

## Starting Profile

**Background going in:**
- Dedicated university courses in Calculus and Linear Algebra — comfortable with derivatives, limits, matrix operations, eigenvalues
- No Probability/Statistics coursework at the start (Aug 2026). Probability calculus runs at university in winter 2026/27, alongside Phase 1; mathematical statistics follows in summer 2027
- Python basics — can write scripts, understands control flow
- C1 English — can read papers, docs, courses without friction

**Gaps to close before ML work gets serious:**
- Probability and statistics — genuinely new material, not a refresher. Phase 0's math track introduced it (`docs/phase0/math_concepts.md` 1.3); Phase 1's Module 1B covers the ML-relevant statistics before university does.
- Python needs to reach "fluent" level (OOP, clean code, tooling)
- NumPy needs to be second nature
- ML library stack (PyTorch above all) is essentially untouched
- No experience yet with model training pipelines, distributed systems, or deployment

**The honest timeline:** 18 months at 3–4 hrs/day is achievable to reach junior/mid ML Engineer level competitive for roles at serious AI labs — but only if you are consistent and project-driven, and only if each phase has a real deadline. Open-ended phases expand to fill the time available.

---

## The Big Picture — All 6 Phases

```
Phase 0 │ Foundations Refresh         │ ~8 weeks (done, 2026-09-27)
Phase 1 │ ML Theory + Classical ML    │ ~9 weeks (target 2026-11-29)
Phase 2 │ Deep Learning Core          │ ~10 weeks
Phase 3 │ LLMs & Transformers         │ ~12 weeks
Phase 4 │ MLOps & Systems             │ ~8 weeks
Phase 5 │ Frontier Work & Portfolio   │ ongoing
```

These phases overlap in practice. Don't treat them as strict sequential blocks — once you start Phase 2, you keep coding Python. Once you start Phase 3, you keep reading papers.

---

## PHASE 0 — Foundations Refresh
### Target date: **September 27, 2026** (~8 weeks from Aug 3, 2026) — **completed 2026-09-27** | Goal: Arrive at Phase 1 with zero weak spots holding you back

This date is fixed, not aspirational. University restarts in October and your daily hours drop — Phase 0 needs to be behind you before then. If you're not done by the target date, **cut remaining scope** (drop a stretch project, skip an exercise section you're already comfortable with) rather than slip the date. An unfinished Phase 0 that ends on time beats a "complete" one that eats into semester 3.

The goal here isn't to master everything — it's to remove blockers. You have the math. You have basic Python. This phase upgrades both to the level required for serious ML work.

### What's in Phase 0
- **Concepts**: Python (OOP, functions, error handling, types, project structure, git) + NumPy (arrays, indexing, broadcasting, linear algebra, einsum, numerical stability) + Matplotlib (plot types, subplots, saving figures) + Math (linear algebra, calculus/backprop intuition, probability). Full teaching content in `docs/phase0/python_concepts.md`, `numpy_concepts.md`, `matplotlib_concepts.md`, `math_concepts.md`.
- **Drills**: 36 NumPy exercises, 24 Python exercises (several multi-part) — predict-before-run methodology. See `docs/phase0/python_exercises.md` and `numpy_exercises.md`.
- **Projects**: see `docs/phase0/projects.md` — 4 core projects, done in order, plus one stretch project (Scalar Autograd Engine).
- **Git**: see `docs/GIT_GUIDE.md`.

### 0A — Python: From Mediocre to Fluent

You need Python to feel like a natural extension of your thoughts, not something you have to fight. The ML Engineer stack is almost entirely Python.

**What to focus on:**
- **OOP properly** — classes, inheritance, dunder methods (`__init__`, `__repr__`, `__len__`), decorators (`@property`, `@staticmethod`, `@classmethod`). ML codebases use these constantly.
- **Pythonic idioms** — list/dict/generator comprehensions, `zip`, `enumerate`, `*args/**kwargs`, context managers (`with`), f-strings
- **Error handling** — `try/except`, custom exceptions, logging (not `print`)
- **Modules and packages** — how imports work, how to structure a project with `__init__.py`, relative vs absolute imports
- **Type hints** — `def train(model: nn.Module, lr: float) -> dict:` — standard in modern ML code
- **Virtual environments** — `venv` or `conda`, `requirements.txt`, `pyproject.toml`
- **Git basics** — see `docs/GIT_GUIDE.md`. Non-negotiable for any engineering role.

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
- Linear algebra ops: `np.dot`, `@`, `np.linalg.solve`, `np.linalg.inv`, `np.linalg.eig`, `np.linalg.svd`
- Shape manipulation: `reshape`, `transpose`, `squeeze`, `expand_dims`, `stack`, `concatenate`
- Reduction ops: `sum`, `mean`, `std`, `max`, `argmax` along specific axes
- `np.einsum` — one notation for dot products, matmul, batched matmul, attention-score patterns
- Numerical stability — overflow/underflow in `exp`/`log`, the subtract-max trick (softmax, log-sum-exp)

**Resources:**
- The official NumPy "Absolute Beginner's Guide" + "NumPy for Beginners" on numpy.org
- *Python for Data Analysis* by Wes McKinney
- CS231n's Python/NumPy tutorial (cs231n.github.io/python-numpy-tutorial)

### 0C — Math: Confirm and Fill Gaps

Linear algebra and calculus have real university coursework behind them already — this checklist is a targeted refresher for ML-specific angles on that material, not a first exposure. Probability & Statistics is different: genuinely new material, taught from zero in `math_concepts.md` 1.3, not assumed.

**Linear Algebra (critical — highest priority in all of ML):** matrix multiplication/transpose/inverse, dot products and cosine similarity, eigenvalues/eigenvectors, SVD, vector spaces/basis/rank/null space, norms (L1, L2, Frobenius).

**Calculus (for backpropagation):** partial derivatives and the gradient, chain rule (this IS backprop), Jacobians/Hessians (conceptual), Taylor series.

**Probability & Statistics (new material — built from zero):** random variables and distributions, Bernoulli/Categorical/Gaussian, expectation/variance/covariance, Bayes' theorem, MLE, KL divergence and cross-entropy as loss functions.

**Resources (fill gaps only):**
- *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong — free PDF at mml-book.github.io
- 3Blue1Brown's "Essence of Linear Algebra" — YouTube
- Gilbert Strang's MIT OCW Linear Algebra — if you want the rigorous treatment

---

## PHASE 1 — ML Theory + Classical ML
### Target date: **November 29, 2026** (~9 weeks from Sept 28, 2026) | Goal: Understand how ML works at the algorithmic and statistical level

Full plan, reading map and specs: `docs/phase1/README.md`. Six modules (30 sections in total):

- **1A — pandas & SQL:** DataFrames, cleaning, groupby/merge/reshape, pandas 3 Copy-on-Write, EDA, SQL via DuckDB.
- **1B — Statistics for ML:** estimators, bias/variance, confidence intervals, bootstrap, hypothesis testing, MLE ↔ loss functions.
- **1C — Workflow & evaluation:** train/val/test, cross-validation, leakage, bias–variance tradeoff, metrics, calibration, imbalance, scikit-learn pipelines and tuning.
- **1D — Linear models:** regression with inference, Ridge/Lasso/Elastic Net, logistic/softmax regression (from scratch), feature engineering.
- **1E — Trees & ensembles:** CART (from scratch), random forests, gradient boosting, XGBoost/LightGBM, feature importance.
- **1F — Other methods & unsupervised:** k-NN, SVMs, Naive Bayes, PCA, clustering.

GD/SGD, learning rate, L2 regularization and MSE/cross-entropy were covered in Phase 0 — revisited here only where new.

**Resources:** *An Introduction to Statistical Learning with Applications in Python* (ISLP, free) as the theory spine; *Hands-On Machine Learning with Scikit-Learn and PyTorch* (Géron, 2025), Part I, as the practice spine. pandas user guide, *Python for Data Analysis* (McKinney, 3rd ed.), scikit-learn user guide, StatQuest.

**Projects for Phase 1:**
1. Data project — clean and analyse a real, messy dataset with pandas and SQL.
2. From-scratch models — logistic regression, CART, a small gradient booster, each verified against scikit-learn.
3. Capstone — end-to-end tabular ML on a real dataset: EDA, leakage-proof pipeline, cross-validation, 3+ model families, tuning, one final test evaluation, error analysis, written report. First portfolio piece.

---

## PHASE 2 — Deep Learning Core
### Duration: ~10 weeks | Goal: Train neural networks confidently in PyTorch

### 2A — Neural Networks from First Principles
The neuron, layers and depth, activation functions (ReLU, GELU), forward pass, backprop (mathematically), weight initialization (Xavier/Kaiming), batch norm, dropout.

**Resources:** Andrej Karpathy's "Neural Networks: Zero to Hero" (the single best resource — watch all of it). *Understanding Deep Learning* by Simon Prince (free, udlbook.github.io) as the theory book. *Hands-On Machine Learning with Scikit-Learn and PyTorch* (Géron), Part II — continues Phase 1's book. 3Blue1Brown "Neural Networks" series. *Deep Learning* (Goodfellow et al., 2016) as a reference only.

### 2B — PyTorch
Tensors, `torch.autograd`, `nn.Module`, core layers, loss functions, optimizers, the training loop (`zero_grad → forward → loss → backward → step`), `DataLoader`/`Dataset`, GPU usage, saving/loading models.

**Resources:** Official PyTorch tutorials ("Learn the Basics"). Karpathy's makemore repo (micrograd's ground is already covered by `microtensor`).

**Projects for Phase 2:**
1. From-scratch project — replacement to be decided when Phase 2 is planned. The original "MLP from scratch (micrograd)" is already done: Phase 0's Project 4 (NumPy network, manual backprop) and stretch project `microtensor` (scalar autograd). Candidates: array-based autograd engine, or reimplementing core PyTorch pieces (`nn.Module`, optimizer) to understand its internals.
2. CNN image classifier on CIFAR-10 in PyTorch, full custom training loop.
3. Reproduce a small paper (LeNet, a simple RNN LM, or a basic VAE).

### 2C — Important Architectures
CNNs (convolution, pooling, ResNet), RNNs/LSTMs (vanishing gradients), autoencoders/VAEs, embeddings.

### 2D — Reinforcement Learning Fundamentals (bridge to Phase 3)
MDPs, returns, policy gradients (REINFORCE), advantage/baselines, PPO intuition. Needed for Phase 3's post-training (GRPO/RLVR) — nothing else in the roadmap teaches it.

**Resources:** Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., free), ch. 13 (policy gradients). Exact resources confirmed when Phase 2 is planned.

---

## PHASE 3 — LLMs & Transformers
### Duration: ~12 weeks | Goal: Deeply understand how frontier language models are built

### 3A — The Transformer Architecture
Read *"Attention Is All You Need"* (Vaswani et al., 2017) — twice, once before and once after the concepts below. Tokenization (BPE, SentencePiece), embeddings + positional encoding, self-attention (`softmax(QKᵀ/√d_k)V`), causal masking, multi-head attention, feed-forward layers, layer norm, residual connections, encoder vs decoder blocks, scaling laws (Chinchilla).

**Resources:** Karpathy's "Let's build GPT from scratch" (mandatory) and his nanochat repo (Oct 2025 — full pipeline: tokenizer, pretraining, SFT, RL, chat inference). *The Illustrated Transformer* by Jay Alammar. Sebastian Raschka's LLM writeups. Research blogs from major AI labs (Anthropic, OpenAI, DeepMind, etc.).

### 3B — Training Language Models
Pre-training (next-token prediction, data curation, gradient accumulation, mixed precision, distributed training basics — DDP, model/pipeline/tensor parallelism, ZeRO), post-training (SFT; preference optimization — RLHF with PPO as the historical baseline, DPO; RL with verifiable rewards — GRPO and variants, as used for reasoning models; Constitutional AI / RLAIF; distillation), parameter-efficient fine-tuning (LoRA/QLoRA).

**Resources:** Hugging Face course and TRL docs. LoRA (arxiv 2106.09685), DPO, Chinchilla, DeepSeek-R1 (GRPO) papers.

### 3C — Key Ecosystem Tools
Hugging Face Transformers/Datasets, PEFT, TRL, vLLM, LangChain/LlamaIndex (know what they do, don't obsess).

**Projects for Phase 3:**
1. Build a GPT from scratch (nanoGPT, character-level), then run the full nanochat pipeline at small scale — non-negotiable.
2. Fine-tune an open-source LLM (7B class) with LoRA via Hugging Face + PEFT.
3. Toy post-training: GRPO on a small model with a verifiable reward (e.g. arithmetic), compared against DPO on preference data.

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
Inference optimization (vLLM, SGLang, TensorRT-LLM, ONNX; continuous batching, paged KV cache), REST APIs (FastAPI), batch inference, model versioning.

**Project for Phase 4:** Deploy your fine-tuned LLM from Phase 3 as a REST API (FastAPI + vLLM), containerized with Docker, with wandb tracking and at least some unit tests. Full GitHub README.

---

## PHASE 5 — Frontier Work & Portfolio
### Duration: Ongoing from month ~16

### 5A — Reading Research Papers
How to read a paper (abstract/conclusion → figures → intro → methods → experiments). Build a reading list over time covering architecture foundations, training techniques, efficiency/systems, and alignment/safety — pull from arxiv.org, Papers With Code, and lab research blogs as you go, rather than committing to a fixed list now.

### 5B — Open Source Contributions
Start small (docs, examples, tests) in a major ML repo (e.g. Hugging Face Transformers). Graduate to implementing a paper or improving a training script.

### 5C — Portfolio Strategy
Tier 1 (Phases 0–2): from-scratch implementations, classical ML pipeline, CNN classifier.
Tier 2 (Phase 3): GPT from scratch (nanoGPT/nanochat), fine-tuned LLM with LoRA, toy GRPO/DPO post-training.
Tier 3 (Phase 4): deployed model API, experiment tracking, distributed training or quantization work.
Tier 4 (Phase 5): paper reproduction with your own analysis, an original experiment, a write-up explaining something you learned deeply.

**Blog:** Write about what you learn — for clarity, not marketing. If you can explain self-attention from first principles in writing, you understand it.

### 5D — Staying Current
Follow major lab research blogs, Hugging Face Blog, Karpathy, Sebastian Raschka's newsletter, and similar. Weekly habit: 30 minutes skimming arxiv abstracts (cs.LG, cs.CL) on Fridays, read one paper properly per week.

---

## Parallel Tracks (Run Alongside Everything)

**Data Structures & Algorithms:** structured path, not random LeetCode — one reading + 2–3 problems/week, from Phase 1 on. Plan and progress: `docs/dsa/README.md`.

**Linear Algebra Deepening:** eigendecomposition in the context of PCA, SVD in the context of LoRA, optimization theory.

**English Technical Writing:** commit messages, docstrings, READMEs, eventually paper/technique explanations.

---

## Recommended Full Resource Stack (Prioritized)

**Books:** *Mathematics for Machine Learning* (free PDF), *An Introduction to Statistical Learning with Applications in Python* (free PDF), *Hands-On Machine Learning with Scikit-Learn and PyTorch* (Géron, 2025), *Understanding Deep Learning* (Prince, free PDF), *Fluent Python* (Ramalho), *Problem Solving with Algorithms and Data Structures using Python* (free online). *Deep Learning* (Goodfellow, free PDF) as a reference.

**Video courses:** Karpathy "Neural Networks: Zero to Hero", Fast.ai "Practical Deep Learning", Hugging Face Course, CS231n Stanford, DeepLearning.AI short courses.

**Practice platforms:** Kaggle, Hugging Face Hub, Google Colab / Kaggle Notebooks (free GPU).

---

## Month-by-Month Suggested Schedule

| Month | Primary Focus | Side Track |
|-------|--------------|------------|
| 1–2 | Phase 0 (Aug 3 – Sept 27, completed) | Git, CLI tools |
| 3 | Phase 1: pandas, statistics, evaluation | DSA track (from Sept 28) |
| 4 | Phase 1: models + capstone (target Nov 29) | DSA |
| 5 | Phase 2: neural nets, PyTorch core | Read first papers |
| 6 | Phase 2: CNN project, architectures (uni exam session late Jan) | Reproduce a paper |
| 7 | Phase 2 wrap: RL fundamentals | Fast.ai |
| 8 | Phase 3: Transformers + attention, GPT from scratch | Attention paper |
| 9 | Phase 3: nanochat pipeline, Hugging Face ecosystem | GPT-2/3, Chinchilla papers |
| 10 | Phase 3: fine-tuning (LoRA project) | LoRA paper |
| 11 | Phase 3 wrap: post-training — DPO, GRPO | DeepSeek-R1, alignment papers |
| 12 | Phase 4: MLOps — Docker, wandb, tracking | Flash Attention |
| 13 | Phase 4: Deployment — FastAPI, vLLM | Open source contribution |
| 14 | Phase 4: distributed training concepts | DeepSpeed docs |
| 15 | Phase 4 wrap: evaluation, red-teaming, safety | System cards |
| 16 | Phase 5: original research experiment | Paper writing |
| 17 | Phase 5: portfolio polish, applications | Interview prep |
| 18 | Interview rounds, networking, open source | Stay current |

Month 1 = August 2026. Semester workload checked 2026-09-28 — 3–4 hrs/day holds for Phase 1. Rows from month 5 on are re-checked when each phase is planned.

---

## Interview Preparation (Start Month 15–16)

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

*Last updated: 2026-09-30*
