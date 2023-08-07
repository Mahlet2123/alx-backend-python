#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    that measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n.

    Your function should return a float.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n
