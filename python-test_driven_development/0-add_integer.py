#!/usr/bin/python3
"""Module for adding two integers a and b together"""


def add_integer(a, b=98):
    """adds a + b

        a = int/float
        b = int/float, def int 98

        Returns: sum a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
