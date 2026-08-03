"""
Project 3 — Linear Regression from Scratch.

LinearRegression class in pure NumPy, built in stages:
1. Closed-form OLS (np.linalg.lstsq, not inv — more stable)
2. Batch gradient descent
3. Mini-batch gradient descent
4. Ridge regression (L2, don't regularize the bias term)

Test on synthetic data (recover known weights) and California Housing
(sklearn) — expect R^2 ~0.5-0.7. See docs/PHASE0_PROJECTS.md for the full
spec and "done when" criteria.
"""
