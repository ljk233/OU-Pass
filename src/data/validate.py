"""data.validate_data.py
"""

from abc import abstractmethod
from typing import Any

import pandas as pd


class DataValidator:
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def get_shape(self) -> tuple[int, int]:
        """Return the shape of the data."""
        pass

    @abstractmethod
    def get_number_of_missing_values(self) -> int:
        """"""
        return self.data.isna().sum().sum()

    @abstractmethod
    def get_feature_names(self) -> dict[str, str]:
        """Return the data's features and their datatypes."""
        pass

    @abstractmethod
    def get_feature_dtypes(self) -> dict[str, str]:
        """Return the data's features and their datatypes."""
        pass

    def run(self, params: dict[str, Any]):
        """Return the data's features and their datatypes."""
        expected_shape = tuple(params["shape"])
        assert (
            self.get_shape() == expected_shape
        ), f"Data has unexpected shape {self.get_shape()}"

        expected_num_missing = params["num_missing"]
        assert (
            self.get_number_of_missing_values() == expected_num_missing
        ), f"Data has unexpected number of missing values"

        expected_feature_names = set(params["features"].keys())
        assert (
            self.get_feature_names().difference(expected_feature_names) == set()
        ), f"Data has unexpected column names {self.get_feature_names()}"

        expected_feature_dtypes = params["features"]
        for feature, dtype in self.get_feature_dtypes().items():
            assert (
                dtype == expected_feature_dtypes[feature]
            ), f"Data has unexpected feature data type {feature}: {dtype}"


class PandasDataValidator(DataValidator):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, data: pd.DataFrame):
        """"""
        self.data: pd.DataFrame = data

    def get_shape(self) -> tuple[int, int]:
        """Return the shape of the data."""
        return self.data.shape

    def get_number_of_missing_values(self) -> int:
        """"""
        return self.data.isna().sum().sum()

    def get_feature_names(self) -> set[str]:
        """Return the data's features and their datatypes."""
        return set(self.data.columns.values)

    def get_feature_dtypes(self) -> dict[str, str]:
        """ """
        observed_feature_dypes = self.data.dtypes.astype(str).to_dict()
        mapped_feature_dtypes = {}
        for feature, dtype in observed_feature_dypes.items():
            if dtype in set(["int32", "int64"]):
                mapped_feature_dtypes[feature] = "int"
            elif dtype in set(["object", "category"]):
                mapped_feature_dtypes[feature] = "object"
            else:
                raise ValueError(f"dtype {dtype} is not mapped.")

        return mapped_feature_dtypes


def create_data_validator(backend: str) -> DataValidator:
    """"""
    match backend:
        case "pandas":
            return PandasDataValidator
