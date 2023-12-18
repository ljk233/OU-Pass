"""data/cleaners.py

Purpose
-------

This module provides concrete data cleaners for specific data formats.

Classes
-------

- `PandasCleaner`: Concrete cleaner class for Pandas DataFrames.
"""

import pandas as pd

from ._base import cleaner


class PandasDataCleaner(cleaner.Cleaner):
    """Concrete data cleaner class for Pandas DataFrames.

    Inherits from the `cleaner.Cleaner` class, implementing data cleaning
    and column renaming specific to Pandas DataFrames.
    """

    def __init__(self):
        """Initalise a `PandasDataCleaner` instance."""
        super().__init__()

    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean and rename specific columns in the provided Pandas DataFrame.

        Args:
            data: The Pandas DataFrame to be cleaned.

        Returns:
            The cleaned Pandas DataFrame.
        """
        return data.drop(columns="exam_score").rename(
            columns={
                "mod_result": "did_pass",
                "continous_ass_score": "cma_score",
                "age": "estimated_age",
            }
        )


def create_cleaner(backend: str) -> cleaner.Cleaner:
    """Create a data cleaner based on the specified backend.

    Args:
        backend: The data backend (e.g., "pandas").

    Returns:
        A data cleaner instance based on the specified backend.

    Raises:
        `NotImplementedError` if the specified backend is not supported.
    """
    match backend:
        case "pandas":
            return PandasDataCleaner()
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")
