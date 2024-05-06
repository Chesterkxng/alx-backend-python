#!/usr/bin/env python3
"""
Import wait_random and write an async routine called wait_n that takes in 2 int
arguments . You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    look-up for definition
    """
    sorted_delay: List[float] = []
    for i in range(n):
        sorted_delay.append(await task_wait_random(max_delay))
    return sorted(sorted_delay)
