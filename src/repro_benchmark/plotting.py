from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

def plot_results(results_csv: Path, out_png: Path) -> Path:
    df = pd.read_csv(results_csv)
    # Simple bar chart: accuracy per dataset/model
    pivot = df.pivot(index="dataset", columns="model", values="accuracy")
    ax = pivot.plot(kind="bar")
    ax.set_ylabel("accuracy")
    ax.set_title("Benchmark accuracy by dataset/model")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()
    return out_png
