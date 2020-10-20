#!/usr/bin/env python3

"""
6. Complex types - mixed list
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float.
    """
    return k, v * v
