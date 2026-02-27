# repro-benchmark

A small, **reproducible** command-line tool to run baseline ML benchmarks, export results, and generate a minimal report.

This project is designed to be **JOSS-friendly**: clear install/run steps, deterministic outputs (fixed seeds), tests, and a short paper (`paper.md`).

## Install

```bash
python -m pip install -U pip
pip install -e .
```

## Quick start

Run a benchmark (Iris + Wine datasets; Logistic Regression + Random Forest):

```bash
repro-benchmark run --outdir outputs
```

Create a summary table:

```bash
repro-benchmark summarize --outdir outputs
```

Make a plot:

```bash
repro-benchmark plot --outdir outputs
```

Generate a report:

```bash
repro-benchmark report --outdir outputs
```

You should end up with:

- `outputs/results.csv` (per dataset/model metrics)
- `outputs/summary.csv` (aggregated)
- `outputs/plot.png`
- `outputs/report.md`

## Reproducibility

All splits and models use fixed seeds by default (`--seed 0`).

## License

MIT — see `LICENSE`.

## How to cite

See `CITATION.cff` and the JOSS paper in `paper.md`.
