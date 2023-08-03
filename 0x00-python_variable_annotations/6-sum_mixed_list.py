#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """ sum of floats and integers in a list"""
    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
