from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

from .data import Dataset

@dataclass(frozen=True)
class RunConfig:
    seed: int = 0
    test_size: float = 0.2

def _fit_predict_lr(X_train, y_train, X_test, seed: int):
    # Deterministic; increase max_iter for stability.
    model = LogisticRegression(max_iter=3000, random_state=seed, n_jobs=None)
    model.fit(X_train, y_train)
    return model.predict(X_test)

def _fit_predict_rf(X_train, y_train, X_test, seed: int):
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=seed,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    return model.predict(X_test)

def run_benchmark(datasets: List[Dataset], cfg: RunConfig) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for ds in datasets:
        X_train, X_test, y_train, y_test = train_test_split(
            ds.X,
            ds.y,
            test_size=cfg.test_size,
            random_state=cfg.seed,
            stratify=ds.y,
        )
        for model_name, fn in [
            ("logreg", _fit_predict_lr),
            ("rf", _fit_predict_rf),
        ]:
            y_pred = fn(X_train, y_train, X_test, cfg.seed)
            rows.append({
                "dataset": ds.name,
                "model": model_name,
                "n_train": int(len(y_train)),
                "n_test": int(len(y_test)),
                "accuracy": float(accuracy_score(y_test, y_pred)),
                "f1_macro": float(f1_score(y_test, y_pred, average="macro")),
                "seed": int(cfg.seed),
                "test_size": float(cfg.test_size),
            })
    return pd.DataFrame(rows)

def summarize(results: pd.DataFrame) -> pd.DataFrame:
    # Simple aggregation: mean metrics per model over datasets
    agg = (
        results
        .groupby(["model"], as_index=False)
        .agg(
            accuracy_mean=("accuracy", "mean"),
            f1_macro_mean=("f1_macro", "mean"),
            datasets=("dataset", "nunique"),
        )
        .sort_values(["accuracy_mean", "f1_macro_mean"], ascending=False)
        .reset_index(drop=True)
    )
    return agg
