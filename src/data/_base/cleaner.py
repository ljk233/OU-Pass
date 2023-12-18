"""data/_base/cleaner.py

Purpose
-------

This module defines the foundation for data cleansing using abstract base
classes and concrete classes. It provides an abstract base class,
AbstractCleaner, that defines the core interface and a concrete base class
that defines a default initialisation method.

Classes
-------

`AbstractCleaner`:

- Represents the base class for all data clensing implementations.
- Provides abstract methods for data cleansing.

`DataValidator`:

- A concrete implementation of the `AbstractCleaner` class.
- Provides a default implementation for the `__init__` method.
- If a concrete class inherits from this class, then only specific only
implementations are needed, but the `__init__` method can also be extended
if wanted.
"""

from abc import ABC, abstractmethod


class AbstractCleaner(ABC):
    """Abstract base class for data cleaning.

    Defines the core methods for data cleaning tasks.
    """

    @abstractmethod
    def clean_data(self, data):
        """Clean the data.

        Args:
            data: The data to be cleaned.

        Returns:
            The cleaned data.
        """
        pass


class Cleaner(AbstractCleaner):
    """Concrete class for data cleaning.

    Provides a default __init__() method for specific implementation.
    """

    def __init__(self):
        """Initialise an instance of Cleaner."""
        pass
