#!/usr/bin/python3
"""Write a function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of methods and attributes of an object

    Args: an object

    Returns: a string list of all methods and attributes of an object
    """
    return dir(obj)
