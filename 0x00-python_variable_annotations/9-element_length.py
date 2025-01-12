from typing import Iterable, Sequence, Tuple
"""Iterable Object"""


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    """Return a tuple"""
    return ((i, len(i)) for i in lst)
