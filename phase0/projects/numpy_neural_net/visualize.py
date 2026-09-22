from pathlib import Path
import matplotlib.pyplot as plt

FIGURES_DIR = Path(__file__).parent / "figures"


def plot_training_curves(train_loss: list[float], val_accuracy: list[float]) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax1.plot(train_loss)
    ax1.set_title("Train loss")
    ax1.set_ylabel("loss (cross-entropy)")

    ax2.plot(val_accuracy)
    ax2.set_title("Val accuracy")
    ax2.set_xlabel("epoch")
    ax2.set_ylabel("accuracy")
    fig.savefig(FIGURES_DIR / "training_curves.png")
