#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return sum as float"""
    return float(sum(mxd_list))
