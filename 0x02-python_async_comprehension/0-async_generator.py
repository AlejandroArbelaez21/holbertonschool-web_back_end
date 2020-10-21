#!/usr/bin/env python3

"""
0. The basics of async
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10
    """
    for _ in range(10):
        number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield number
