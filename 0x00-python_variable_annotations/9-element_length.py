#!/usr/bin/env python3

"""
8. Complex types - functions
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    return [(i, len(i)) for i in lst]
