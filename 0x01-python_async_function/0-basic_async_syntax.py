#!/usr/bin/env python3
"""
Generate asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Generate a float between 0 and 10 and wait
    an equivalent time before returning it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
