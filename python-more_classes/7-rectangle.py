#!/usr/bin/python3
"""A class for Rectangles"""


class Rectangle:
    """The Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """defines the str() string representation of the class"""

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for _ in range(self.__height):
                rect += "{}".format(Rectangle.print_symbol) * self.__width
                if _ != self.__height - 1:
                    rect += '\n'
            return rect

    def __repr__(self):
        """defines the repr() representation of the class"""

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """only hits upon deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
