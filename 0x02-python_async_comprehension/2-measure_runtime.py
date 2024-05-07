#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel
using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ look-up for def
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )
    return time.perf_counter() - start_time
