"""data/_base/validator.py

Purpose
-------

This module defines the foundation for data validation using abstract base
classes and concrete classes. It provides an abstract base class,
AbstractValidator, that defines the core validation methods for data
shape, missing values, feature names, and data types.

Recommendation
--------------

All specific implementations should inherit from the concrete `Validator`.

Extending the DataValidator
---------------------------

- Inherit from `DataValidator`.
- Implement the abstract methods.
- Override `validate_data`, calling `super().__init__(data, schema)` first
and then add any other validations needed.

Classes
-------

`AbstractValidator`:

- Represents the base class for all data validation implementations.
- Provides abstract methods for basic data validation

`DataValidator`:

- A concrete implementation of the `AbstractValidator` class.
- Provides a default implementation for the `__init__()` method and `validate_data()`
- Specific implementations should implement the abstract methods.
"""

from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    """Abstract base class for data validation."""

    @abstractmethod
    def get_shape(self) -> tuple[int, int]:
        """Get the data's shape (number of rows, number of columns)."""
        raise NotImplementedError()

    @abstractmethod
    def get_number_of_missing_values(self, data) -> int:
        """Get the total number of missing values in the data."""
        raise NotImplementedError()

    @abstractmethod
    def get_feature_names(self, data) -> dict[str, str]:
        """Get the names of the features in the data."""
        raise NotImplementedError()

    @abstractmethod
    def get_feature_dtypes(self, data) -> dict[str, str]:
        """Get the datatypes of the features in the data."""
        raise NotImplementedError()

    @abstractmethod
    def validate_data(self, data, schema: dict):
        """Validate the data against the specified schema.

        Args:
            data: The data to be validated.
            schema: The schema against which the data should be validated.

        Raises:
            ValueError: If the data does not conform to the schema.
        """
        raise NotImplementedError()


class Validator(AbstractValidator):
    """Implements data validation using the defined schema."""

    def __init__(self):
        pass

    def validate_data(self, data, schema: dict):
        """Validate the data against the specified schema.

        Args:
            data: The data to be validated.
            schema: The schema against which the data should be validated.

        Raises:
            ValueError: If the data does not conform to the schema.
        """
        observed_shape = self.get_shape(data)
        expected_shape = tuple(schema["shape"])
        assert observed_shape == expected_shape, f"Data has unexpected shape."

        observed_num_missing = self.get_number_of_missing_values(data)
        expected_num_missing = schema["num_missing"]
        assert (
            observed_num_missing == expected_num_missing
        ), f"Data has unexpected number of missing values."

        observed_feature_dtypes = self.get_feature_dtypes(data)

        observed_feature_names = set(observed_feature_dtypes.keys())
        expected_feature_names = set(schema["features"].keys())
        assert (
            observed_feature_names == expected_feature_names
        ), f"Data has unexpected column names."

        expected_feature_dtypes = schema["features"]
        for feature, dtype in observed_feature_dtypes.items():
            assert (
                dtype == expected_feature_dtypes[feature]
            ), f"Data has unexpected feature data type."
