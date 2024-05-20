#!/usr/bin/python3
"""write json to file"""
import json


def save_to_json_file(obj, filename):
    """write json to file
    Args:
    filename- file in question
    obj- the object to write
    Returns- no return"""
    with open(filename, mode="w", encoding="utf-8") as f:
        dat = json.dumps(obj)
        f.write(dat)
