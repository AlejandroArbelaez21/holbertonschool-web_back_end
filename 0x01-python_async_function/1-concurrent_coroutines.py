#!/usr/bin/env python3

"""
0. The basics of async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay, n) -> List[float]:
    """
    an asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay
    """
    list_num: List[float] = []
    for number in range(n):
        list_num.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(list_num)]
