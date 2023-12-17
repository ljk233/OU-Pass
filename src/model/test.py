"""model/test.py
"""

from abc import abstractmethod
from typing import Any

import scipy.stats as st
from sklearn import linear_model, metrics
import statsmodels.api as sm
import pandas as pd

from .train import Dataset


LogisticRegression = linear_model.LogisticRegression


class ModelTester:
    @abstractmethod
    def run(self, params: dict[str, Any]) -> Any:
        pass


class StatsModelTester(ModelTester):
    def __init__(self, model: LogisticRegression, test_data: Dataset):
        self.model = model
        self.data: Dataset = test_data
        self.X_constant = sm.add_constant(self.data.X)

    def predict_with_model(self):
        prob_preds = self.model.predict(self.X_constant)
        y_pred = [st.bernoulli(prob_pred).rvs() for prob_pred in prob_preds]

        return y_pred

    def predict_without_model(self):
        return st.bernoulli(0.1).rvs(self.data.y.shape[0])

    def build_confusion_matrix(self):
        ...

    def plot_roc(self):
        ...

    def run(self) -> Any:
        """_summary_"""
        # Sort the observed values
        y_true = list(self.data.y)

        # Make predictions
        y_pred_model = self.predict_with_model()
        y_pred_no_model = self.predict_without_model()

        # Sort the true and previcted values
        sorted_true, sorted_pred_model, sorted_pred_no_model = [
            sorted(values) for values in [y_true, y_pred_model, y_pred_no_model]
        ]

        # Compare the observed values to the predicted values
        num_correct_model = 0
        for true, pred in zip(sorted_true, sorted_pred_model):
            num_correct_model += true == pred

        num_correct_no_model = 0
        for true, pred in zip(sorted_true, sorted_pred_no_model):
            num_correct_no_model += true == pred

        # Calculate the accuracies
        model_accuracy = 100 * num_correct_model / len(self.data.y)
        no_model_accuracy = 100 * num_correct_no_model / len(self.data.y)

        # Return the accuracies
        return {
            "with model": f"{model_accuracy:.2f}%",
            "without model": f"{no_model_accuracy:.2f}%",
        }

        return f"Accuracy of predicted number of left-footed players: {100 * accuracy:.2f}%"

        # Get the number observed and expected
        # num_observed = sum(self.data.y)
        # num_expected = sum(y_pred_model)
        # num_obs_exp_map = {"num_observed": num_observed, "num_expected": num_expected}

        # num_difference = num_expected - num_observed

        # Confusion matrix
        confusion_matrix = pd.DataFrame(
            metrics.confusion_matrix(self.data.y, y_pred_model, normalize="true"),
            index=pd.Index(["is_left_footed", "is_not_left_footed"], name="actual"),
            columns=pd.Index(
                ["is_left_footed", "is_not_left_footed"], name="predicted"
            ),
        )
        print(confusion_matrix)

        return

        # ROC curve


def create_model_tester(backend: str) -> ModelTester:
    match backend:
        case "sklearn":
            return None
        case "statsmodels":
            return StatsModelTester
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")
