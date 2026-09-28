# Phase 1 — Classical ML

**Target date: November 29, 2026** (~9 weeks from 2026-09-28, 3–4 hours/day). Status tracker: `phase1/README.md`. Plan context: `docs/ROADMAP.md` Phase 1.

Goal: understand how ML works at the algorithmic and statistical level, and run a leakage-proof, honestly-evaluated tabular ML project end to end.

---

## How this phase works

- **Two books, both read, not re-written here.** ISLP for the statistical view and theory, Géron for scikit-learn practice and engineering habits. Section docs in this folder are reading guides: which chapters when, plus short notes only where the books are thin or where material connects back to Phase 0.
- **Build it, then use the library** — continued from Phase 0. Logistic regression, a decision tree, and a small gradient booster get written from scratch and checked against scikit-learn before relying on scikit-learn's versions.
- **Drills stay predict-before-run** (as in `docs/phase0/numpy_exercises.md`). Section specs, drills, and project specs are written one section at a time, right before each section starts.
- **Probability runs in parallel at university** (Rachunek prawdopodobieństwa, winter 2026/27; midterm 2026-12-04). Phase 1 leans on it and doesn't re-teach it. Mathematical statistics comes at university only next semester, so section 1B covers the ML-relevant statistics here.

## Resources

| Resource | Use | Access |
|---|---|---|
| *An Introduction to Statistical Learning with Applications in Python* (ISLP) — James, Witten, Hastie, Tibshirani, Taylor | Theory spine | Free PDF, statlearning.com |
| *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Géron (2025), Part I (ch. 1–8) | Practice spine; Part II carries into Phase 2 | O'Reilly |
| pandas user guide (pandas 3.x) + *Python for Data Analysis*, 3rd ed. — McKinney | pandas | Free online |
| scikit-learn user guide (1.9+) | API reference, evaluation chapter | Free online |
| StatQuest (YouTube) | Visual intuition per topic | Free |
| *Introduction to Probability* — Blitzstein & Hwang | Probability backup, alongside the uni course | Free PDF |

## Sections

| Section | Topics | Reading | Time |
|---|---|---|---|
| **1A — pandas & SQL** | Series/DataFrame, `.loc`/`.iloc`, dtypes (incl. pandas 3 `str` dtype), missing data, groupby/aggregation, merge/join, reshape (pivot/melt), datetimes, Copy-on-Write; EDA with seaborn; SQL (SELECT, WHERE, GROUP BY, JOIN, window functions) on DataFrames/Parquet via DuckDB | McKinney ch. 5–10; pandas user guide; Géron ch. 2 (data part) | ~1.5 wk |
| **1B — Statistics for ML** | Estimators and their bias/variance, standard errors, confidence intervals, bootstrap, hypothesis testing basics, MLE — and why MSE is the Gaussian MLE and cross-entropy the Bernoulli/Categorical MLE (Phase 0's `math_concepts.md` 1.3, now applied) | ISLP 2.1–2.2, 3.1.2, 5.2, 13.1; StatQuest | ~1 wk |
| **1C — Workflow & evaluation** | Problem framing, train/val/test, cross-validation (k-fold, stratified, grouped, time-based), data leakage, bias–variance tradeoff, learning curves, metrics (regression; classification: confusion matrix, precision/recall/F1, ROC-AUC, PR-AUC, log loss, calibration), class imbalance, baselines; scikit-learn estimators/transformers, `Pipeline`, `ColumnTransformer`, hyperparameter search | Géron ch. 1–3; ISLP ch. 2, 5; scikit-learn "Model selection and evaluation" | ~1.5 wk |
| **1D — Linear models** | Linear regression with inference, Ridge/Lasso/Elastic Net, logistic and softmax regression (logistic from scratch), feature engineering (scaling, encoding, interactions, polynomial features) | ISLP ch. 3, 4, 6 (7 skim); Géron ch. 4 | ~1 wk |
| **1E — Trees & ensembles** | CART decision tree (from scratch), bagging, random forests, gradient boosting (concept + small from-scratch version), XGBoost/LightGBM/CatBoost in practice, feature importance (impurity vs. permutation, SHAP overview) | ISLP ch. 8; Géron ch. 5–6; StatQuest gradient boosting series | ~1.5 wk |
| **1F — Other methods & unsupervised** | k-NN, SVMs (margins, kernels), Naive Bayes, PCA, clustering beyond k-means (hierarchical, DBSCAN, Gaussian mixtures) | ISLP ch. 9, 12; Géron ch. 7–8 | ~1 wk |

## Projects

1. **Data project** (after 1A, a few days) — clean and analyse a real, messy dataset with pandas and SQL.
2. **From-scratch models** (across 1D–1E) — logistic regression, CART tree, small gradient booster in one package, each verified against scikit-learn.
3. **Capstone** (~1.5 wk, end of phase) — end-to-end tabular ML on a real dataset: EDA, leakage-proof pipeline, cross-validation, 3+ model families, tuning, one final test evaluation, error analysis, written report. Optional: compare against a tabular foundation model (TabPFN).

Full specs: `docs/phase1/projects.md`, written before each project starts.

## Out of scope

Polars (mentioned in 1A, not drilled), time series forecasting, deep learning (Phase 2).

---

*Last updated: 2026-09-28*
