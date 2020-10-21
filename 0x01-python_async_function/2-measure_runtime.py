#!/usr/bin/env python3

"""
2. Measure the runtime
"""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time
    """
    init_time = time()
    asyncio.run(wait_n(n, max_delay))
    final_time = time()
    total_time = init_time - final_time
    return total_time / n
