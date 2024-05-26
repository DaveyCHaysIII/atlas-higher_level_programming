#!/usr/bin/python3
"""class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """set width"""
            self.__width = value
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")

        @property
        def height(self):
            """getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """set height"""
            self.__height = value
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")

        @property
        def x(self):
            """getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """set x"""
            self.__x = value
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be > 0")

        @property
        def y(self):
            """getter"""
            return self.__y

        @y.setter
        def y(self, value):
            """set y"""
            self.__y = value
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be > 0")
