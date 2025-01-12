#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple, List
"""Iterable Object"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a tuple"""
    return ((i, len(i)) for i in lst)
