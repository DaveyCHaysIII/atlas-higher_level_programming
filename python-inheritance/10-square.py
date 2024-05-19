#!/usr/bin/python3
"""write a class Square that inherits from Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class to describe Squares
    inherits from Rectangles

    private args: 
    size - size of Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        return self.__size ** 2
