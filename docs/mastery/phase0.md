# Phase 0 — Mastery Log

This is not a completion tracker — `phase0/README.md` already does that (sections/projects done or not). This is a separate, honest record of how *deeply* the load-bearing concepts inside those completed sections actually landed, backed by specific evidence rather than "the exercise is checked off." Completing an exercise and understanding it are different facts; this file is where that difference gets written down instead of silently assumed.

Not every concept in Phase 0 gets an entry — only ones that later phases genuinely depend on, or ones where the real difficulty of learning them turned out to be a useful signal.

## Scale

`Exposed` → `Practiced` → `Understood` → `Implemented` → `Applied` → `Verified` → `Mastered`

- **Exposed** — read about it, hasn't been exercised yet.
- **Practiced** — attempted it, needed significant hints or scaffolding to get through it.
- **Understood** — can restate the idea in different words, ideally without prompting.
- **Implemented** — working code exists and passes its tests.
- **Applied** — used inside a larger project, not just an isolated exercise.
- **Verified** — checked against an independent method (finite-difference gradient check, a known closed-form answer, etc.), not just "it ran without error."
- **Mastered** — several of the above, sustained across more than one context, without help.

Most entries below sit in the middle of this scale. That's expected for Phase 0 — it's the honest state, not a problem to hide.

---

## NumPy — Numerical Stability & ML Patterns (Sections 7–8)

- **Subtract-max trick (softmax / log-sum-exp)** — *Verified*, 2026-09-01. Own `log_sum_exp` implementation was missing the `+ np.max(x)` correction term, caught during review and fixed; the corrected version was later reused inside `cross_entropy_from_logits` and gradient-checked there.
- **Sigmoid / tanh stable formulas (split-by-sign)** — *Implemented*, 2026-09-02. Correct, passing code for both, but only after extensive from-zero explanation of *why* the naive versions overflow (including why tanh fails worse than sigmoid — both tails overflow, producing `nan` via `inf/inf`, vs. sigmoid's one-sided failure that happens to still resolve correctly). Understanding was reconstructed live, not self-generated first.
- **Cross-entropy — binary, categorical, and from-logits** — *Understood, not yet Applied*, 2026-09-03/2026-09-05. Needed a full ground-up rebuild — one-hot encoding, normalized probabilities, then the `log(softmax(x))_c = x_c - logsumexp(x)` identity — across three separate rounds before `cross_entropy_from_logits` was implemented correctly (passing its `logits_good < logits_bad` test). Has not yet been used inside an actual training loop.
- **k-means clustering** — *Implemented*, 2026-09-05. Final code passes all tests (correct labels, `[50,50,50]` cluster sizes, inertia strictly decreasing `850.68 → 297.95`), but only after three real bugs were found and fixed (`range(2)` hardcoded instead of `range(k)`, a missing `return` statement, and inertia measured at the wrong point in the loop — after the centroid update instead of before, which silently hid the real improvement). Needed a fully worked numeric trace (6 points, 2 iterations, every intermediate array printed) before the algorithm's mechanics made sense. Treat as fragile until it reappears in a new context unprompted.
- **Gradient of ReLU, MSE, and a linear layer** (`relu_gradient`, `mse_gradient`, `linear_layer_gradients`) — *Verified*, 2026-09-02. Implemented, then confirmed against an independent finite-difference gradient check (`np.allclose(num_grad, anal_grad) → True`) rather than just "it ran."

## Math — Probability Foundations

- **Random variables, PMF/PDF, Bernoulli, Categorical, Gaussian** — *Exposed*, 2026-09-05. Written into `math_concepts.md` 1.3 today, in direct response to discovering there was no prior probability/statistics coursework to build on (the roadmap had wrongly assumed otherwise). Not yet exercised — first real test will be whether the Bernoulli-as-binary-cross-entropy and Categorical-as-softmax connections get used unprompted in Project 4.

## Project 3 — Linear Regression from Scratch (in progress)

- **Linear regression as `y = Xw + b`** — *Understood*, 2026-09-05. Initially explained (wrongly) via assumed econometrics background; rebuilt from plain slope/intercept algebra (`y = mx + c`) once that assumption was corrected. Could then correctly restate what `w` and `b` represent, but a follow-up mistake (`score` calling `r_squared(X, y)` directly instead of predicting first) shows the model/metric boundary isn't fully solid yet.
- **Closed-form OLS via `np.linalg.lstsq` + augmented-ones trick** — *Verified*, 2026-09-05. Implemented, then confirmed by recovering exactly known `w = [2, -1]`, `b = 3.0` from synthetic data with `score() == 1.0`, after two real bugs were found and fixed (`X[0]` used instead of `X.shape[0]`; non-idiomatic `rcond=False` instead of `rcond=None`).
- **Method chaining (`return self`)** — *Implemented*, 2026-09-05. Unfamiliar pattern; understood immediately once shown a working-vs-broken comparison, then applied correctly in `fit()` without further correction needed.
- **Gradient descent, ridge regularization, optimizer comparison** — not yet started.

## Earlier Sections (Python 1–7, NumPy 1–4)

Completed and tagged (`p0-python-s1`…`s7`, `p0-numpy-s1`…`s4`) before this log existed. No concept-level evidence was recorded at the time, so no entries are backfilled here rather than guessing — this file starts recording forward from 2026-09-05. If any of that material resurfaces and turns out shakier than the tag implies, it gets an honest entry here when that happens, not before.

---

*Last updated: 2026-09-05*
