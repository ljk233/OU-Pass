"""data/_base/validator.py

Purpose
-------

This module defines abstract base classes for data validation, providing
a foundation for creating reusable and consistent data validation logic.

`AbstractDataValidator` Class

The `AbstractDataValidator` class serves as an interface for data validation,
defining abstract methods for retrieving data shape, number of missing values,
feature names, feature datatypes, and validating the data against a schema.
This ensures consistent behavior and allows for different implementations
of data validation logic without compromising the interface.

`DataValidator` Class

The `DataValidator` class inherits from the `AbstractDataValidator` and
provides concrete implementations for the abstract methods. It also defines
the `validate_data` method, which performs the core data validation logic
by checking the data against the expected schema. This encapsulates the
validation process and ensures consistency across different data validation
implementations.

`Specific Validators`

Specific data validation classes, such as those for different data formats,
inherit from the `DataValidator` class and provide concrete implementations
for the remaining methods. These methods handle the retrieving of specific
data characteristics, such as the data shape, number of missing values, feature
names, and feature datatypes. By keeping these implementations specific to the
data format, the `DataValidator` class remains agnostic to the underlying data
format and ensures consistent validation logic for various data types.

This combination of abstract base classes and specific validators enables
developers to create reusable and maintainable data validation classes for
different data formats without compromising the consistency and effectiveness
of the validation process.
"""

from abc import ABC, abstractmethod


class AbstractDataValidator(ABC):
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


class DataValidator(AbstractDataValidator):
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
