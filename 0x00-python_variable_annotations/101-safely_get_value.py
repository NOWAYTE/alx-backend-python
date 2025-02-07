#!/usr/bin/env python3
"""Type annotations"""

from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None]) -> Union[Any, T]:
    """Returns a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
