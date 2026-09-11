import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

FIGURES_DIR = Path(__file__).parent / "figures"


def plot_loss_curves(batch_losses: list[float], minibatch_losses: list[float]) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots()
    ax.plot(batch_losses, label="batch GD")
    ax.plot(minibatch_losses, label="mini-batch GD")
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss (MSE)")
    ax.set_title("Batch vs Mini-batch GD - Loss curves")
    ax.legend()
    fig.savefig(FIGURES_DIR / "loss_curves.png")


def plot_predictions_vs_truth(y_true: np.ndarray, y_pred: np.ndarray) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots()
    ax.scatter(y_true, y_pred)
    lo = min(y_true.min(), y_pred.min())
    hi = max(y_true.max(), y_pred.max())
    ax.axline([lo, lo], [hi, hi])
    ax.set_xlabel("true values")
    ax.set_ylabel("predicted values")
    ax.set_title("True vs Predicted values")
    fig.savefig(FIGURES_DIR / "predictions.png")


def plot_weight_convergence(weight_history: np.ndarray) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots()
    for i in range(weight_history.shape[1]):
        ax.plot(weight_history[:, i], label=f"w{i}")
    ax.set_xlabel("epochs")
    ax.set_ylabel("weights")
    ax.set_title("Weight convergence over epochs")
    ax.legend()
    fig.savefig(FIGURES_DIR / "weight_convergence.png")
