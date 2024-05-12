#!/usr/bin/python3
"""Trying out validation on class creation"""


class Square:
    """class with attr size that MUST be 0"""

    try:
        def __init__(self, size=0):
            self.size = size
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
