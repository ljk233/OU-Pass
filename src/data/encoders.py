"""data/encoders.py

This module provides concrete data encoders for specific data formats.
Pandas is to read CSV files so the data types can be preserved.

Classes
-------

- `CSVEncoder`: Concrete encoder class for handling CSV files.
- `PandasEncoder`: Concrete encoder class for handling Pandas DataFrames.
"""

import csv

import pandas as pd

from ._base import encoder


class CSVEncoder(encoder.Encoder):
    """Concrete encoder class for handling CSV files."""

    def __init__(self):
        """Initialises the encoder."""
        super().__init__()

    def decode(self, data: list[dict], path: str) -> None:
        """Converts the given list of dicts into a CSV file.

        Args:
            data: The data to be decoded.
            path: The path to the output CSV file.
        """
        pd.DataFrame(data).to_csv(path, index=False)

    def encode(self, path: str) -> list[dict]:
        """Converts data from a CSV file into a list of dicts.

        Args:
            path: The path to the CSV file to be encoded.

        Returns:
            The decoded data as a list of dicts.
        """
        encoded_data = pd.read_csv(path).to_dict(orient="records")

        return encoded_data


class PandasEncoder(encoder.Encoder):
    """Concrete encoder class for handling Pandas DataFrames."""

    def __init__(self):
        """Initialises the encoder."""
        super().__init__()

    def decode(self, data: list[dict]) -> pd.DataFrame:
        """Converts the given list of dicts into a Pandas DataFrame.

        Args:
            data: The data to be decoded.

        Returns:
            The decoded data in a Pandas DataFrame.
        """
        return pd.DataFrame(data)

    def encode(self, data: pd.DataFrame) -> list[dict]:
        """Converts the given data into a list of dicts.

        Args:
            data: The data to be encoded.

        Returns:
            The data as a list of dicts.
        """
        return data.to_dict(orient="records")


def create_encoder(fmt: str) -> encoder.Encoder:
    """Creates an encoder instance for the specified data format.

    Args:
        fmt: The data format to be created.

    Returns:
        An encoder instance for the specified data format.

    Raises:
        NotImplementedError: If the specified data format is not supported.
    """
    match fmt:
        case "csv":
            return CSVEncoder()
        case "pandas":
            return PandasEncoder()
        case _:
            raise NotImplementedError(f"Encoding of {fmt} is not supported.")
