#!/usr/bin/python3
"""Trying out validation on class creation"""


class Square:
    """class with attr size that MUST be 0"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method to return area of square"""

        return self.__size * self.__size
