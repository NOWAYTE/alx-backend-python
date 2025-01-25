#!/usr/bin/env python3
"""Iterable object"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a List"""
    return ((i, len(i)) for i in lst)
