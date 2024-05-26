#!/usr/bin/python3
"""test"""


class Base:
    """class Base"""
    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += self.__nb_objects + 1
