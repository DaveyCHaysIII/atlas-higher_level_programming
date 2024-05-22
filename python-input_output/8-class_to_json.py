#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """function that returns a dictionary
    Args:
    obj- the object in question
    Returns- a dictionary"""
    return obj.__dict__
