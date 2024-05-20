#!/usr/bin/python3
"""write json to file"""
import json


def save_to_json_file(obj, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        dat = json.dumps(obj)
        f.write(dat)
