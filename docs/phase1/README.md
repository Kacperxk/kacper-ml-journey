# Phase 1 — Classical ML

**Target date: November 29, 2026** (~9 weeks from 2026-09-28, 3–4 hours/day). Status tracker: `phase1/README.md`. Plan context: `docs/ROADMAP.md` Phase 1.

Goal: understand how ML works at the algorithmic and statistical level, and run a leakage-proof, honestly-evaluated tabular ML project end to end.

---

## How this phase works

Same shape as Phase 0: **modules** (like Phase 0's Python and NumPy) split into numbered **sections**, each with drills.

| Per module | File | Written |
|---|---|---|
| Concepts: reading guide + notes | `docs/phase1/<module>_concepts.md` | When the module starts |
| Drills, grouped by section | `docs/phase1/<module>_exercises.md` | When the module starts |
| Your answers, one notebook per section | `phase1/<module>/section<N>_<topic>.ipynb` | By you |
| Project specs | `docs/phase1/projects.md` | Before each project starts |

- **The books teach; the concepts docs guide.** Each concepts section says what to read (ISLP, Géron, McKinney, docs), then adds short notes only where the books are thin, out of date (e.g. McKinney predates pandas 3), or where material connects back to Phase 0.
- **Every module has code drills**, including statistics: its drills check theory by simulation (sampling distributions, bootstrap, permutation tests) in NumPy/SciPy.
- **Drills are predict-before-run**, as in `docs/phase0/numpy_exercises.md`. Every written task ends in `assert`s.
- **Build it, then use the library** — continued from Phase 0: logistic regression, a CART tree, and a small gradient booster are built from scratch in Project 2 and checked against scikit-learn.
- **Probability runs in parallel at university** (Rachunek prawdopodobieństwa, winter 2026/27; midterm 2026-12-04). Module 1B assumes none of it has been covered yet (decided 2026-09-30): it teaches the probability it needs — random variables, expectation/variance, common distributions, likelihood — from Blitzstein & Hwang. Mathematical statistics comes at university only next semester, so Module 1B covers the ML-relevant statistics here.

## Resources

| Resource | Use | Access |
|---|---|---|
| *An Introduction to Statistical Learning with Applications in Python* (ISLP) — James, Witten, Hastie, Tibshirani, Taylor | Theory spine (1B–1F) | Free PDF, statlearning.com |
| *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Géron (2025), Part I (ch. 1–8) | Practice spine (1C–1F); Part II carries into Phase 2 | O'Reilly |
| *Python for Data Analysis*, 3rd ed. — McKinney | pandas (1A) | Free online, wesmckinney.com/book |
| pandas (3.x), seaborn, DuckDB, scikit-learn (1.9+) docs | API reference | Free online |
| StatQuest (YouTube) | Visual intuition per topic | Free |
| *Introduction to Probability* — Blitzstein & Hwang | Probability for 1B, ahead of the uni course | Free PDF |

## Modules

### 1A — pandas & SQL · `phase1/pandas/` · ~1.5 weeks

1. Series & DataFrame fundamentals
2. Indexing, selection & Copy-on-Write
3. Cleaning: missing data, dtypes, strings
4. Transforming & groupby
5. Combining: concat & merge
6. Reshaping & time
7. EDA & visualization
8. SQL with DuckDB

### 1B — Statistics for ML · `phase1/stats/` · ~1 week

1. Sampling & estimators — sampling distributions, bias, variance, MSE of an estimator
2. Maximum likelihood — and why MSE / cross-entropy are MLE losses
3. Confidence intervals & the bootstrap
4. Hypothesis testing — p-values, permutation tests, multiple testing

Reading: ISLP 2.1–2.2, 3.1.2, 4.3.2, 5.2, 13.1–13.3; StatQuest.

### 1C — Workflow & evaluation · `phase1/evaluation/` · ~1.5 weeks

1. The scikit-learn API — estimators, transformers, `Pipeline`, `ColumnTransformer`
2. Splitting & cross-validation — train/val/test, k-fold, stratified, grouped, time-based; leakage
3. Metrics — regression; confusion matrix, precision/recall/F1, ROC/PR curves, log loss, calibration
4. Bias–variance, learning & validation curves, hyperparameter search
5. Imbalanced data & baselines

Reading: Géron ch. 1–3; ISLP ch. 2, 5; scikit-learn "Model selection and evaluation".

### 1D — Linear models · `phase1/linear_models/` · ~1 week

1. Linear regression as inference — standard errors, confidence intervals, diagnostics
2. Regularization — Ridge, Lasso, Elastic Net
3. Logistic & softmax regression
4. Feature engineering — encoding, scaling, interactions, polynomial features

Reading: ISLP ch. 3, 4, 6 (7 skim); Géron ch. 4.

### 1E — Trees & ensembles · `phase1/trees/` · ~1.5 weeks

1. Decision trees — splitting criteria, depth, overfitting
2. Bagging & random forests
3. Gradient boosting — concept, XGBoost/LightGBM, early stopping
4. Interpreting models — impurity vs. permutation importance, partial dependence, SHAP overview

Reading: ISLP ch. 8; Géron ch. 5–6; StatQuest gradient boosting series.

### 1F — Other methods & unsupervised · `phase1/other_methods/` · ~1 week

1. k-NN & the curse of dimensionality
2. Support vector machines
3. Naive Bayes
4. PCA
5. Clustering — k-means, hierarchical, DBSCAN, Gaussian mixtures

Reading: ISLP ch. 9, 12; Géron ch. 7–8, Appendix C (SVMs).

## Projects · `phase1/projects/`

1. **Data project** (after 1A, a few days) — clean and analyse a real, messy dataset with pandas and SQL.
2. **From-scratch models** (across 1D–1E) — logistic regression, CART tree, small gradient booster in one package, each verified against scikit-learn.
3. **Capstone** (~1.5 wk, end of phase) — end-to-end tabular ML on a real dataset: EDA, leakage-proof pipeline, cross-validation, 3+ model families, tuning, one final test evaluation, error analysis, written report. Optional: compare against a tabular foundation model (TabPFN).

## Out of scope

Polars (mentioned in 1A, not drilled), time series forecasting, deep learning (Phase 2).

---

*Last updated: 2026-09-30*
