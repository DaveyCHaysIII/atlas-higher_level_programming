#!/usr/bin/python3
"""Write class student"""


class Student:
    """Student class
    first_name
    last_name
    age
    to_json method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary rep of Student"""
        return self.__dict__
