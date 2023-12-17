"""data.make_dataset.py
"""

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class DataCleaner(ABC):
    @abstractmethod
    def run(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Clean the data."""
        pass


class PandasDataCleaner(DataCleaner):
    def __init__(self, data: list[dict[str, Any]]):
        """_summary_"""
        self.data: pd.DataFrame = pd.DataFrame(data)

    def run(self, params: dict[str, Any]) -> list[dict[str, Any]]:
        """_summary_"""
        # Select columns
        # ==============
        selected_data = self.data[params["selected_columns"].keys()]

        # Handle missing values
        # =====================
        # We replace the empty string due to how it was ingested
        no_nulls_data = selected_data.replace("", None).dropna(how="any")

        # Set the data types
        typed_data = no_nulls_data
        for column, column_info in params["selected_columns"].items():
            match column_info["dtype"]:
                case "int":
                    typed_data[column] = typed_data[column].astype(int)
                case _:
                    pass

        # Rename the columns
        # ==================

        # Gather the new name is a dict
        remapper = {}
        for column, column_info in params["selected_columns"].items():
            remapper[column] = column_info["name"]

        renamed_data = typed_data.rename(columns=remapper)

        return renamed_data


def create_data_cleaner(backend: str) -> DataCleaner:
    match backend:
        case "pandas":
            return PandasDataCleaner
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")
