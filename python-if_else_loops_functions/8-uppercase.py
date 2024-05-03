#!/usr/bin/python3

def uppercase(str):
    upper_string = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        upper_string += upper_char
    print(upper_string)
