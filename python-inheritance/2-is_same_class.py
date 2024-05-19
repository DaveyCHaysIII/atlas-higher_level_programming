#!/usr/bin/python3
"""a function that returns True if the object is
exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a):
    """
    Returns True if obj is a member of a_class
    otheriwse false

    Args:
    obj - an instance of a class
    a_class - a specific class

    Returns: True, False
    """
    if type(obj) is a:
        return True
    else:
        return False
