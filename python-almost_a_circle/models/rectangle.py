#!/usr/bin/python3
"""class Rectangle"""
Base = __import__('base').Base


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

        @property
        def height(self):
            """getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """set height"""
            self.__height = value

        @property
        def x(self):
            """getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """set x"""
            self.__x = value

        @property
        def y(self):
            """getter"""
            return self.__y

        @y.setter
        def y(self, value):
            """set y"""
            self.__y = value
