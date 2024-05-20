#!/usr/bin/python3
"""Write a function that appends (UTF-8) a file"""


def append_write(filename="", text=""):
    """Append text to file
    Args:
    filename- file in question
    text- text to write
    returns: number of characters written"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
