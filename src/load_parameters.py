"""src/load_parameters.py

Module for loading parameters from a TOML file.

This module provides a function to load parameters from a TOML file and
returns either the entire set of parameters or a specific key-value pair.

Functions:
- `load_parameters(path: str, name: str | None = None) -> dict[str, Any]`
"""

import tomllib
from typing import Any


def load_parameters(path: str, name: str | None = None) -> dict[str, Any]:
    """
    Loads parameters from a TOML file.

    Args:
        path: Path to the TOML file containing the parameters.
        name: The name of the parameter to retrieve. If `None`, returns
        the entire set of parameters. Default is `None`.

    Returns:
        A dictionary containing the parameters, or the value associated
        with the specified key if `name` is provided.

    Raises:
        ValueError: If the specified key is not found in the TOML file.

    Examples:
        ```python
        # Load the entire set of parameters
        all_parameters = load_parameters("parameters.toml")

        # Load a specific subset of parameters
        cleaning_parameters = load_parameters("parameters.toml", "cleaning")
        ```
    """

    with open(path, "rb") as f:
        parameters = tomllib.load(f)

    if name and name not in parameters:
        raise ValueError(f"Arg {name} is not a key in the TOML file.")

    return parameters if name is None else parameters.get(name)
