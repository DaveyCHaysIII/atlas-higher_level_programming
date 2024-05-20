#!/usr/bin/python3
"""print a pascal triangle"""


def pascal_triangle(n):
    """Print a pascal triangle
    Args:
    n- number of rows
    Returns: list of lists of integers"""
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
