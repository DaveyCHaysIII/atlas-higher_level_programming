#!/usr/bin/python3
"""test to see if obj merely inherits
from type a"""


def inherits_from(obj, a):
    """Returns if obj merely inherits
    from a, but is not an instance of a

    Args:
    obj- the object in question
    a - the class tested agains

    Returns: true, false"""

    if isinstance(obj, a) and type(obj) is not a:
        return True
    else:
        return False
