#!/usr/bin/python3

Rectangle = __import__('rectangle').Rectangle

R1 = Rectangle(3, 4, 0, 0, 5)

R1.width = 7

print(R1.width)
print(R1.height)