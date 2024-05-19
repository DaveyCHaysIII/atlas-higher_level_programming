#!/usr/bin/python3
"""Create a base class base_geometry"""


class BaseGeometry():
    """
    Create a BaseGeometry class
    with a method defining area
    with a method validating integers
    """

    def area(self):
        """function to define area

        Args:
        self - the instance

        Returns: exception (area is not implemented)"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integers passed into class

        Args:
        self - self
        name - always string
        value - always integer

        Returns: Err if val is not integer, err if val is <0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name, end=""))
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name, end=""))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name, end=""))
