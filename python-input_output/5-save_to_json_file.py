#!/usr/bin/python3
"""write json to file"""
import json


def save_to_json_file(obj, filename):
    """write json to file
    Args:
    filename- file in question
    obj- the object to write
    Returns- no return"""
    dat = json.dumps(obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(dat)
