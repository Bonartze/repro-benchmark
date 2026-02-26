---
title: "repro-benchmark: one-command, deterministic baseline benchmarking for small ML experiments"
tags:
  - reproducibility
  - benchmarking
  - machine learning
authors:
  - name: YOUR NAME
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: 2026-02-26
bibliography: paper.bib
---

## Summary

Reproducible baselines are essential in computer science research, yet many small experiments are hard to re-run due to ad hoc scripts, missing seeds, or inconsistent result export.
`repro-benchmark` provides a minimal command-line workflow that runs deterministic baseline models on standard toy datasets, exports results to CSV, produces a simple plot, and generates a lightweight Markdown report.

## Statement of need

Researchers frequently need a fast, repeatable way to (i) sanity-check an environment, (ii) compare baseline models, or (iii) demonstrate end-to-end reproducibility.
While full-featured experiment trackers exist, a compact “one command” tool is useful for small projects, tutorials, replication packages, and continuous integration checks.
`repro-benchmark` emphasizes deterministic execution (fixed random seeds), standard exports, and a short path from raw results to a human-readable report.

## Functionality

The tool ships with a CLI:

- `run`: executes Logistic Regression and Random Forest baselines on Iris and Wine datasets, writing `results.csv`.
- `summarize`: aggregates metrics into `summary.csv`.
- `plot`: renders `plot.png` from results.
- `report`: builds `report.md` combining summary, detailed results, and the plot.

All steps operate on files in a user-specified output directory, supporting simple automation and integration into CI pipelines.

## Example

```bash
repro-benchmark run --outdir outputs
repro-benchmark summarize --outdir outputs
repro-benchmark plot --outdir outputs
repro-benchmark report --outdir outputs
```

The generated report includes a summary table (mean accuracy and macro-F1 across datasets) and a figure visualizing accuracy by dataset/model.

## References
Ivan Kirilin