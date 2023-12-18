"""data/_base/encoder.py

Purpose
-------

This module defines the base classes for encoders, which are used to convert
data between different formats. It provides an abstract base class,
`AbstractEncoder`, and a concrete implementation, `Encoder`, that serves as a
foundation for creating encoders for specific data formats.

Recommendation
--------------

We strongly recommend that a shared universal in-memory data structure be
agreed upon before development. This will ensure a consistent and standardised
format for all data exchanged between different encoders.

By adopting a shared data structure, encoders can focus solely on encoding
and decoding data into and out of this universal format, simplifying their
implementation and promoting interoperability.

Benefits of a Unified Data Structure
------------------------------------

Enhanced Interoperability:

A shared data structure promotes interoperability between encoders, allowing
them to seamlessly exchange data without data formatting discrepancies.

Simplified Encoder Implementation:

By focusing on encoding and decoding a standardized data format, encoder
development becomes more straightforward and consistent.

Improved Data Handling:

A unified data structure facilitates consistent data handling across different
components of the data processing pipeline.

Classes
-------

`AbstractEncoder`:

- Represents the base class for all encoder implementations.
- Provides abstract methods for encoding and decoding data.
- If a concrete class inherits from this class, then specific implementations
of the `__init__` and abstract methods are needed.

`Encoder`:

- A concrete implementation of the `AbstractEncoder` class.
- Provides the default implementation for the `__init__` method.
- If a concrete class inherits from this class, then only specific only
implementations are needed, but the `__init__` method can also be extended
if wanted.
"""

from abc import ABC, abstractmethod


class AbstractEncoder(ABC):
    """Base class for all encoder implementations."""

    @abstractmethod
    def decode(self):
        """Decodes data from a universal format into a specific format.

        Raises:
            NotImplementedError: This method must be implemented by concrete
            encoder classes.
        """
        raise NotImplementedError

    @abstractmethod
    def encode(self):
        """Encodes data from a specific format into a universal format.

        Raises:
            NotImplementedError: This method must be implemented by concrete
            encoder classes.
        """
        raise NotImplementedError


class Encoder(AbstractEncoder):
    """Concrete base class for encoders."""

    def __init__(self):
        """Initialises the encoder."""
        pass
