# Phase 0 — Engineering Habits and Tools

Debugging habits, math-to-code habits, learning habits, and editor setup.
Applies across Python, NumPy, and the projects — not specific to one section.

---

## Engineering Habits

**Read the full traceback.** The last line tells you what failed. The lines above it tell you where the code was when it failed and how it got there. Read all of it.

**Use a debugger.** In VS Code: click in the gutter to set a breakpoint, press F5 to run in debug mode. Inspect every variable at any point. 10x faster than print statements. Use it from week one.

**`ipdb` in the terminal:**
```python
import ipdb; ipdb.set_trace()   # add anywhere — drops into interactive mode
```

**Name things precisely.** `x` is fine on paper. In code, use `input_features`, `learning_rate`, `batch_predictions`. You will thank yourself debugging code you wrote three weeks ago.

**Write docstrings before implementing.** Write what the function does before writing the function body. Forces you to think about the interface first.

```python
def r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute R² (coefficient of determination).

    R² = 1.0: perfect predictions.
    R² = 0.0: model just predicts the mean.
    R² < 0.0: model is worse than predicting the mean.

    Args:
        y_true: Ground truth values, shape (n,)
        y_pred: Predicted values, shape (n,)

    Returns:
        R² score as a float.
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return 1 - ss_res / ss_tot
```

**Commit often.** If you have written 30 minutes of code without committing, you are overdue. Small commits with clear messages are always better than large commits with vague ones.

## Math-to-Code Habits

**Work out shapes before writing code.** For every matrix operation, write the shapes explicitly:
```
X:      (100, 3)   — 100 samples, 3 features
W:        (3, 5)   — linear layer
output: (100, 5)   — X @ W
```
Do this before writing the code. This prevents the majority of shape bugs.

**Test on tiny examples first.** Before running on 10,000 samples, verify on 3 samples where you can compute the answer by hand.

**Formula → code immediately.** For every equation you encounter, implement it in NumPy in the same session. Do not let formulas stay abstract.

## Learning Habits

**The rubber duck method.** When stuck, explain the problem out loud or in writing as if to someone who knows nothing. You will often identify the issue while explaining.

**Timebox confusion.** Stuck for more than 25 minutes? Write down exactly what you tried and what happened. Search with those specific terms. Give it 15 more minutes. If still stuck, ask — here, StackOverflow, Discord ML communities.

**Spaced repetition.** Use Anki (apps.ankiweb.net) for things you need to know cold: softmax formula, what a Jacobian is, broadcasting rules, when to use L1 vs L2 norm. 10 minutes of card review per day.

## VS Code Setup

**Extensions to install:**
- Python (Microsoft) — essential
- Pylance — fast autocomplete and type checking
- Black Formatter — auto-format on save
- Ruff — fast linter (replaces flake8, isort)
- GitLens — see Git blame and history inline
- Jupyter — run notebooks without leaving VS Code

**Settings (Ctrl+Shift+P → "Open User Settings JSON"):**
```json
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.rulers": [88],
    "files.trimTrailingWhitespace": true,
    "python.analysis.typeCheckingMode": "basic"
}
```

**Keyboard shortcuts worth learning:**
- F5 — run in debug mode
- F9 — toggle breakpoint
- Ctrl+Shift+P — command palette
- Ctrl+` — open terminal
- Alt+Up/Down — move current line
- Ctrl+D — select next occurrence of selected text

---

*Last updated: 2026-08-16*
