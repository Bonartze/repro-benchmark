from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .data import load_builtin_datasets
from .core import RunConfig, run_benchmark, summarize
from .plotting import plot_results
from .reporting import make_report_md
from .utils import ensure_dir

def _cmd_run(args: argparse.Namespace) -> int:
    outdir = ensure_dir(Path(args.outdir))
    datasets = load_builtin_datasets()
    cfg = RunConfig(seed=args.seed, test_size=args.test_size)
    df = run_benchmark(datasets, cfg)
    out_csv = outdir / "results.csv"
    df.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv}")
    return 0

def _cmd_summarize(args: argparse.Namespace) -> int:
    outdir = ensure_dir(Path(args.outdir))
    results_csv = outdir / "results.csv"
    df = pd.read_csv(results_csv)
    summ = summarize(df)
    out_csv = outdir / "summary.csv"
    summ.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv}")
    return 0

def _cmd_plot(args: argparse.Namespace) -> int:
    outdir = ensure_dir(Path(args.outdir))
    results_csv = outdir / "results.csv"
    out_png = outdir / "plot.png"
    plot_results(results_csv, out_png)
    print(f"Wrote {out_png}")
    return 0

def _cmd_report(args: argparse.Namespace) -> int:
    outdir = ensure_dir(Path(args.outdir))
    results_csv = outdir / "results.csv"
    summary_csv = outdir / "summary.csv"
    plot_png = outdir / "plot.png"
    report = make_report_md(outdir, results_csv, summary_csv, plot_png)
    print(f"Wrote {report}")
    return 0

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="repro-benchmark", description="Reproducible baseline benchmarking CLI.")
    p.add_argument("--outdir", default="outputs", help="Output directory.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("run", help="Run benchmark and write results.csv")
    pr.add_argument("--seed", type=int, default=0)
    pr.add_argument("--test-size", type=float, default=0.2)
    pr.set_defaults(func=_cmd_run)

    ps = sub.add_parser("summarize", help="Summarize results.csv into summary.csv")
    ps.set_defaults(func=_cmd_summarize)

    pp = sub.add_parser("plot", help="Create plot.png from results.csv")
    pp.set_defaults(func=_cmd_plot)

    prep = sub.add_parser("report", help="Create report.md from results/summary/plot")
    prep.set_defaults(func=_cmd_report)

    return p

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))

if __name__ == "__main__":
    raise SystemExit(main())
