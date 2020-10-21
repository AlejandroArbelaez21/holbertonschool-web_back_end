#!/usr/bin/env python3

"""
2. Run time for four parallel comprehensions
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.
    """
    init_time = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),)
    final_time = time()
    total_time = final_time - init_time
    return total_time
