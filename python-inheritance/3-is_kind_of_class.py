#!/usr/bin/python3
"""check to see if obj is instance of class/subclass a"""


def is_kind_of_class(obj, a):
    """
    Checks if object is instance of
    or inherits from class a

    Args:
    obj - the object in question
    a - class to check against

    Returns: True, False
    """
    return isinstance(obj, a)
