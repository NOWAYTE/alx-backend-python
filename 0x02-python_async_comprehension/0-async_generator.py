#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
