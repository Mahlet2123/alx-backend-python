#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments (in this order): n and max_delay.
    and will spawn wait_random n times with the specified max_delay.
    """
    wait_list = []
    for num_of_wait in range(n):
        wait = wait_random(max_delay)
        wait_list.append(wait)
    delays = await asyncio.gather(*wait_list)
    return sorted(delays)
