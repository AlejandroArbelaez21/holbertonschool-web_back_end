#!/usr/bin/env python3

"""
10. Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    if lst:
        return lst[0]
    else:
        return None
