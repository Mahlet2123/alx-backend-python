#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """
    that takes an integer max_delay and returns a asyncio.Task.
    """
    wait = wait_random(max_delay)
    task = asyncio.create_task(wait)
    return task
