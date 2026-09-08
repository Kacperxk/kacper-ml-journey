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
