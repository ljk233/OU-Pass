"""model/train.py
"""

from abc import abstractmethod
import dataclasses
from typing import Any

from sklearn import linear_model, model_selection
import statsmodels.api as sm
import pandas as pd


@dataclasses.dataclass
class Dataset:
    X: pd.DataFrame
    y: pd.Series


@dataclasses.dataclass
class TrainTest:
    training: Dataset
    testing: Dataset


class ModelTrainer:
    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def test_model(self):
        pass


class SklearnTrainer(ModelTrainer):
    def __init__(self, data: Dataset):
        self.data: Dataset = data

    def run(self) -> linear_model.LogisticRegression:
        model = linear_model.LogisticRegression()
        fit = model.fit(self.data.X, self.data.y)

        return fit


class StatsModelsTrainer(ModelTrainer):
    def __init__(self, data: Dataset):
        self.data: Dataset = data
        self.X_constant = sm.add_constant(self.data.X)

    def run(self):
        model = sm.GLM(self.data.y, self.X_constant, family=sm.families.Binomial())
        fit = model.fit()

        return fit


def create_model_trainer(backend: str) -> ModelTrainer:
    match backend:
        case "sklearn":
            return SklearnTrainer
        case "statsmodels":
            return StatsModelsTrainer
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")


def train_test_split(data: pd.DataFrame, params: dict[str, Any]) -> TrainTest:
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data.to_dict())
    predictors = params["predictors"]
    response = params["response"]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        data[predictors],
        data[response],
        test_size=params["test_size"],
        random_state=params["random_state"],
    )
    return TrainTest(Dataset(X_train, y_train), Dataset(X_test, y_test))
