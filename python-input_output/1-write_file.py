#!/usr/bin/python3
"""Write a function that writes a string (UTF-8) to file"""


def write_file(filename="", text=""):
    """
    Write text to file

    Args:
    filename- file in question
    text- text in question

    Returns: nothing
    """
    with open(filename, 'w') as f:
        return f.write(text)
