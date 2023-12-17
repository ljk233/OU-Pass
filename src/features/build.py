"""features.build_features
"""

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class FeatureBuilder:
    @abstractmethod
    def run(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Clean the data."""
        pass


class PandasFeatureBuilder(FeatureBuilder):
    """ """

    def __init__(self, data: pd.DataFrame):
        """"""
        self.data: pd.DataFrame = data

    def run(self) -> pd.DataFrame:
        # Encode the position and preferred_foot columns
        is_goalkeeper = (
            pd.get_dummies(self.data["position"], drop_first=False)["GK"]
            .astype(int)
            .rename("is_goalkeeper")
        )

        is_left_footed = (
            pd.get_dummies(self.data["preferred_foot"], drop_first=False)["Left"]
            .astype(int)
            .rename("is_left_footed")
        )

        return pd.DataFrame(
            {
                "id": self.data["id"],
                "is_goalkeeper": is_goalkeeper,
                "is_left_footed": is_left_footed,
            }
        )


def create_feature_builder(backend: str) -> FeatureBuilder:
    match backend:
        case "pandas":
            return PandasFeatureBuilder
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")
