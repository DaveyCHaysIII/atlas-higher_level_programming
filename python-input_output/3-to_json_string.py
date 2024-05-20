#!/usr/bin/python3
"""Write a function that returns the JSON of an object"""
import json


def to_json_string(obj):
    """dump obj to JSON
    Args:
    obj- the object in question
    Returns- JSON data"""
    return json.dumps(obj)
