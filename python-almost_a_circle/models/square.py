#!/usr/bin/python3
"""class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle
    Changes:
    width, height are now size and are equal"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string rep of Square"""
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("size must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Updates Square using
        args
        kwargs"""
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
