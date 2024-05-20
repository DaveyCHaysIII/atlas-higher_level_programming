#!/usr/bin/python3
"""load json from file"""
import json


def load_from_json_file(filename):
    """load json from file
    Args:
    filename- file in question
    Return: Object from JSON str"""
    with open(filename, mode="r", encoding="utf-8")as f:
        dat = json.load(f)
        return dat
