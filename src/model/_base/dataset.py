"""model/_base/dataset.py
"""

from abc import ABC
import dataclasses

import pandas as pd


@dataclasses.dataclass
class AbstractDataset(ABC):
    pass


@dataclasses.dataclass
class Dataset(AbstractDataset):
    X: pd.DataFrame
    y: pd.Series

    def __post_init__(self):
        self.Xy = pd.concat([self.X, self.y], axis="columns")


@dataclasses.dataclass
class AbstractDatasets(ABC):
    pass


@dataclasses.dataclass
class Datasets(AbstractDatasets):
    training: AbstractDataset
    testing: AbstractDataset
