#!/usr/bin/env python3

"""
3. Tasks
"""
import asyncio
from time import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    function that measures the total execution time
    """
    return asyncio.create_task(wait_random(max_delay))
