#!/usr/bin/env python3
"""Complex types """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that mulitplies a float by multiplier"""

    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
