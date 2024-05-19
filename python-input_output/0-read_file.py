#!/usr/bin/python3
"""Read a file"""


def read_file(file):
    """Opens, prints every line and closes file"""
    with open(file) as f:
        for line in f:
            print(line, end="")
