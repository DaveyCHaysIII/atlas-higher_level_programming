#!/usr/bin/python3
"""Trying out validation on class creation"""


class Square:
    """class with attr size that MUST be 0"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter for size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to return area of square"""

        return self.__size * self.__size
