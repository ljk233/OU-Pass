"""data/_base/validator.py

Purpose
-------
This module defines the foundation for data validation using abstract base
classes and concrete classes. It provides an abstract base class,
`AbstractValidator`, that defines the core validation methods for data
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
- Abstract base class for data validation.
- Provides abstract methods for basic data validation.

`DataValidator`:
- Concrete implementation of the `AbstractValidator` class.
- Default implementation for `__init__()` and `validate_data()`.
- Specific implementations should implement the abstract methods.

Usage
-----
Developers can use the provided validator classes to perform basic data
validation against a specified schema. To create custom validators, inherit
from `DataValidator` and implement the required methods.

Example
-------
```python
# Example Usage of CustomValidator
from data._base.validator import DataValidator

class CustomValidator(DataValidator):
    def get_shape(self) -> tuple[int, int]:
        # Implement custom logic to get data shape
        pass

    def get_number_of_missing_values(self, data) -> int:
        # Implement custom logic to get the number of missing values
        pass

    # Implement other abstract methods

    def validate_data(self, data, schema: dict):
        super().__init__(data, schema)
        # Add additional custom validations
```
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
        assert observed_shape == expected_shape, (
            f"Observed shape {observed_shape}"
            + f"does not match expected shape {expected_shape}."
        )

        observed_num_missing = self.get_number_of_missing_values(data)
        expected_num_missing = schema["num_missing"]
        assert observed_num_missing == expected_num_missing, (
            f"Observed number of missing values {observed_num_missing}"
            + f"does not match expected {expected_num_missing}."
        )

        observed_feature_dtypes = self.get_feature_dtypes(data)

        observed_feature_names = set(observed_feature_dtypes.keys())
        expected_feature_names = set(schema["features"].keys())
        assert observed_feature_names == expected_feature_names, (
            f"Observed feature names {observed_feature_names} do not match"
            + f"expected feature names {expected_feature_names}."
        )

        expected_feature_dtypes = schema["features"]
        for feature, dtype in observed_feature_dtypes.items():
            assert dtype == expected_feature_dtypes[feature], (
                f"Observed data type for feature {feature} is {dtype},"
                + f"but expected {expected_feature_dtypes[feature]}."
            )
