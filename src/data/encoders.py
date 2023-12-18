"""data/encoders.py

This module provides concrete data encoders for specific data formats,
facilitating the conversion of data between different formats.
Two concrete encoder classes are implemented: `CSVEncoder` for handling
CSV files and `PandasEncoder` for handling Pandas DataFrames.

Classes
-------

- `CSVEncoder`: Concrete encoder class for handling CSV files.
- `PandasEncoder`: Concrete encoder class for handling Pandas DataFrames.

Factory Function
----------------

- `create_encoder(fmt: str) -> encoder.Encoder`: Creates an encoder instance
for the specified data format.

Example
-------

```python
# Example Usage of create_encoder
from data.encoders import create_encoder

# Create a CSVEncoder instance
csv_encoder = create_encoder("csv")

# Create a PandasEncoder instance
pandas_encoder = create_encoder("pandas")
"""

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
        fmt (str): The data format for which to create an encoder.

    Returns:
        encoder.Encoder: An encoder instance for the specified data format.

    Raises:
        NotImplementedError: If encoding for the specified data format is
        not supported.
    """
    match fmt:
        case "csv":
            return CSVEncoder()
        case "pandas":
            return PandasEncoder()
        case _:
            raise NotImplementedError(f"Encoding of {fmt} is not supported.")
