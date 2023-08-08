#!/usr/bin/env python3
""" 0-async_generator """
import asyncio
import random


async def async_generator() -> float:
    """
    loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for i in range(11):
        await asyncio.sleep(1)
        yield random.random()
