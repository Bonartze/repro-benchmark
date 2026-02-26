from __future__ import annotations

from pathlib import Path
import pandas as pd

from repro_benchmark.data import load_builtin_datasets
from repro_benchmark.core import RunConfig, run_benchmark, summarize

def test_run_benchmark_deterministic(tmp_path: Path):
    datasets = load_builtin_datasets()
    cfg = RunConfig(seed=0, test_size=0.2)
    df1 = run_benchmark(datasets, cfg).sort_values(["dataset","model"]).reset_index(drop=True)
    df2 = run_benchmark(datasets, cfg).sort_values(["dataset","model"]).reset_index(drop=True)
    pd.testing.assert_frame_equal(df1, df2)

def test_summarize_shape():
    datasets = load_builtin_datasets()
    df = run_benchmark(datasets, RunConfig(seed=0, test_size=0.2))
    summ = summarize(df)
    assert set(summ.columns) == {"model","accuracy_mean","f1_macro_mean","datasets"}
    assert len(summ) == 2
