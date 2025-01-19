#!/usr/bin/env python3
"""Measure the runtime"""

from asyncio import run
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure average runtime of wait_n"""
    start = time.perf_counter()
    run(wait_n(n, max_delay))
    end = time.perf_counter()

    total = end - start
    return total / n
