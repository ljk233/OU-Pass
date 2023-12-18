"""data/_base/encoder.py

Purpose
-------
This module defines the base classes for encoders, facilitating the conversion
of data between different formats. It introduces an abstract base class,
`AbstractEncoder`, and a concrete implementation, `Encoder`, providing
a foundation for creating encoders tailored to specific data formats.

Recommendation
--------------
It is strongly advised to establish a shared universal in-memory data structure
before development. This ensures a consistent and standardized format for
all data exchanged between different encoders.

Benefits of a Unified Data Structure
------------------------------------
Adopting a shared data structure allows encoders to focus solely on encoding
and decoding data into and out of this universal format. This simplifies their
implementation, promotes interoperability, and contributes to a more maintainable
codebase.

Usage
-----
It is recommended to inherit from the concrete base encoder, `Encoder`.
If additional functionality is required during initialization, override
the `__init__()` method as required.

Classes
-------
`AbstractEncoder` (ABC):
- Represents the base class for all encoder implementations.
- Provides abstract methods for encoding and decoding data.
- Concrete classes inheriting from this class need to implement specific 
`__init__` and abstract methods.

`Encoder`:
- A concrete implementation of the `AbstractEncoder` class.
- Provides a default implementation for the `__init__` method.
- If a concrete class inherits from this class, only specific implementations
are needed, although the `__init__` method can also be extended if desired.

Example
-------

```python
# Example Usage of CustomEncoder
from data._base.encoder import Encoder

class CustomEncoder(Encoder):
    def encode(self, data):
        # Implement custom encoding logic
        return encoded_data

    def decode(self, encoded_data):
        # Implement custom decoding logic
        return decoded_data

# Example usage
custom_encoder = CustomEncoder()

# Perform encoding
data_to_encode = {"example": "data"}
encoded_result = custom_encoder.encode(data_to_encode)

# Perform decoding
decoded_result = custom_encoder.decode(encoded_result)
```
"""

from abc import ABC, abstractmethod
from typing import Any


class AbstractEncoder(ABC):
    """Base class for all encoder implementations."""

    @abstractmethod
    def decode(self, data: Any) -> Any:
        """Decodes data from a universal format into a specific format."""
        raise NotImplementedError

    @abstractmethod
    def encode(self, data: Any) -> Any:
        """Encodes data from a specific format into a universal format."""
        raise NotImplementedError


class Encoder(AbstractEncoder):
    """Concrete base class for encoders."""

    def __init__(self):
        """Initializes the encoder."""
        pass
