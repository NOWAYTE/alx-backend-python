#!/usr/bin/env python3
"""Duck typing first letter of a sequence"""

from typing import List, Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element"""

    if lst:
        return lst[0]
    else:
        return None
