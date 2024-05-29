#!/usr/bin/python3
"""Base class"""

import json


class Base:
    """class Base"""
    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id += Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string of w/e object gets passed in"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON of list_objs to file
        list_objs is a list of instances"""
        filename = cls.__name__ + ".json"
        jsonlist = []
        if list_objs is not None:
            jsonlist = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(jsonlist))

    @staticmethod
    def from_json_string(json_string):
        """Returns list from json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new instance with all attrs set"""
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        if cls.__name__ == "Square":
            new_inst = cls(1)

        new_inst.update(**dictionary)

        return new_inst
