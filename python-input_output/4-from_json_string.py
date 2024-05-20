#!/usr/bin/python3
"""Write a function that returns an object from a JSON string"""
import json


def from_json_string(string):
    """De-stringify JSON
    Args:
    string- the JSON string in question
    Returns- Python Object"""
    return json.loads(string)
