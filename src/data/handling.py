"""data/handling.py

Module for handling data operations with different formats and backends.

This module provides classes and functions for loading and saving data in
various formats, such as CSV and JSON. It also provides a factory function
for creating specific data handlers based on the specified data format and
backend.

**Classes:**

- `AbstractDataHandler`: Abstract base class for data handling operations.
- `DataHandler`: Concrete data handler class that performs common data handling
tasks.
- `CSVPandasDataHandler`: Concrete data handler class for handling CSV files
and Pandas DataFrames.

**Functions:**

- `create_data_handler(format, backend)`: Factory function for creating
a `DataHandler` implementation based on the specified data format and backend.
"""

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class AbstractDataHandler(ABC):
    """Abstract base class for data handling operations.

    This class provides an abstract interface for handling common data I/O tasks.
    Concrete implementations inherit from this class and provide specific
    implementations for different data formats.

    Methods:
        load_data(self, path: str) -> Any:
            Loads the data from the given path.
        save_data(self, data: Any, path: str) -> None:
            Saves the given data to the given path.
    """

    @abstractmethod
    def load_data(self, path: str) -> Any:
        """Loads the data from the given path.

        Args:
            path, str: Path where the data is stored.

        Returns:
            The decoded data in a specific format.
        """
        raise NotImplementedError

    @abstractmethod
    def save_data(self, data: Any, path: str) -> None:
        """Converts the data into a format suitable for saving.

        Args:
            data, Any: Data to be encoded.
            path, str: Path where the data is to be stored.
        """
        raise NotImplementedError


class DataHandler(AbstractDataHandler):
    """Concrete data handler class that performs common data handling tasks.

    This class inherits from `AbstractDataHandler` and implements object
    initialisation. Concrete implementations for specific data formats
    and backends inherit from this class and provide specific implementations.
    """

    def __init__(self):
        """Initialise an instance of DataHandler."""
        pass


class CSVPandasDataHandler(DataHandler):
    """Concrete data handler class for handling CSV files and Pandas DataFrames.

    This class inherits from `DataHandler` and implements the specific
    details for the loading of CSV files into Pandas DataFrames and the
    saving of Pandas DataFrames into CSV format.

    Methods:
        load_data(self, path: str) -> pd.DataFrame:
            Loads the data from the given path.
        save_data(self, data: pd.DataFrame, path: str) -> None:
            Saves the given data to the given path.
    """

    def __init__(self):
        """Initialise an instance of CSVPandasDataHandler."""
        super().__init__()

    def load_data(self, path: str) -> pd.DataFrame:
        """Loads the data from the given path.

        Args:
            path, str: Path where the data is stored.

        Returns:
            The decoded data in a specific format.
        """
        return pd.read_csv(path)

    def save_data(self, data: pd.DataFrame, path: str) -> None:
        """Converts the data into a format suitable for saving.

        Args:
            data, pd.DataFrame: Data to be saved.
            path, str: Path where the data is to be stored.
        """
        data.to_csv(path, index=False)


def create_data_handler(format: str, backend: str) -> DataHandler:
    """Factory function for creating a `DataHandler` implementation based
    on the specified data format and backend.

    Args:
        format, str:
            The format of the data (e.g., "csv", "json").
        backend, str:
            The backend for handling data (e.g., "pandas", "numpy").

    Returns:
        An instance of `DataHandler` corresponding to the specified data
        format and backend.

    Raises:
        NotImplementedError: If the specified format is not supported.
        NotImplementedError: If the specified backend is not supported for
        the given format.
    """
    match format:
        case "csv":
            match backend:
                case "pandas":
                    return CSVPandasDataHandler()
                case _:
                    raise NotImplementedError(
                        f"Handling of {format} | {backend} is not supported."
                    )
        case _:
            raise NotImplementedError(f"Handling of {format} files is not supported.")
