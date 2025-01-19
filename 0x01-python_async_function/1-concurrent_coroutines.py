#!/usr/bin/env python3
"""Multiple coroutines"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns n times with he specified max_delay"""

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)

    return sorted_delays
