#!/usr/bin/python3
"""Write a class Rectangle based on BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class to describe Rectangles

    private args:
    width: integer
    height: integer
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self, width, height):
        return ("[Rectangle]: {}/{}".format(width, height, end=""))

    def area(self):
        return self.width * self.height
