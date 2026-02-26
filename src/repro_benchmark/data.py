from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from sklearn.datasets import load_iris, load_wine

@dataclass(frozen=True)
class Dataset:
    name: str
    X: np.ndarray
    y: np.ndarray

def load_builtin_datasets() -> List[Dataset]:
    iris = load_iris()
    wine = load_wine()
    return [
        Dataset("iris", iris.data, iris.target),
        Dataset("wine", wine.data, wine.target),
    ]
