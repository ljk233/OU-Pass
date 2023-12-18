"""data/validators.py

Purpose
-------
This module provides concrete data validators for specific data formats.

Classes
-------
- `PandasDataValidator`: Concrete validator class for handling Pandas
DataFrames.
"""

import pandas as pd

from ._base import validator


class PandasDataValidator(validator.Validator):
    """Data validation class for Pandas DataFrames."""

    def __init__(self):
        super().__init__()

    def get_shape(self, data: pd.DataFrame) -> tuple[int, int]:
        """Get the data's shape (number of rows, number of columns).

        Args:
            data: A Pandas DataFrame

        Returns:
            Shape of the data (n_rows, n_cols)
        """
        return data.shape

    def get_number_of_missing_values(self, data: pd.DataFrame) -> int:
        """Get the total number of missing values in the data.

        Args:
            data: A Pandas DataFrame

        Returns:
            Number of missing values
        """
        return data.isna().sum().sum()

    def get_feature_names(self, data: pd.DataFrame) -> set[str]:
        """Get the names of the features in the data.

        Args:
            data: A Pandas DataFrame

        Returns:
            Set of feature names
        """
        return set(data.columns.values)

    def get_feature_dtypes(self, data: pd.DataFrame) -> dict[str, str]:
        """Get the datatypes of the features in the data.

        Args:
            data: A Pandas DataFrame

        Returns:
            Dictionary mapping feature -> generic data type
        """
        observed_feature_dtypes = data.dtypes.astype(str).to_dict()
        mapped_feature_dtypes = {}
        for feature, dtype in observed_feature_dtypes.items():
            if dtype in set(["int32", "int64"]):
                mapped_feature_dtypes[feature] = "integer"
            elif dtype in set(["object", "category"]):
                mapped_feature_dtypes[feature] = "string"
            elif dtype in set(["float64"]):
                mapped_feature_dtypes[feature] = "real"
            else:
                raise ValueError(f"Unsupported dtype {dtype} for feature {feature}.")

        return mapped_feature_dtypes


def create_validator(backend: str) -> validator.Validator:
    """Factory function for creating data validators based on the specified
    backend.
    """
    match backend:
        case "pandas":
            return PandasDataValidator()
        case _:
            raise NotImplementedError(
                f"No validator for {backend} has been implemented"
            )
