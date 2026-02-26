from __future__ import annotations

from pathlib import Path

import pandas as pd

def make_report_md(outdir: Path, results_csv: Path, summary_csv: Path, plot_path: Path) -> Path:
    results = pd.read_csv(results_csv)
    summary = pd.read_csv(summary_csv)

    md = []
    md.append("# repro-benchmark report\n")
    md.append(f"Output directory: `{outdir}`\n")
    md.append("## Summary\n")
    md.append(summary.to_markdown(index=False))
    md.append("\n\n## Results\n")
    md.append(results.to_markdown(index=False))
    md.append("\n\n## Plot\n")
    md.append(f"![Benchmark plot]({plot_path.name})\n")

    report_path = outdir / "report.md"
    report_path.write_text("\n".join(md), encoding="utf-8")
    return report_path
