#!/usr/bin/python3
"""this model is for creating a function
pascal_triangle that returns a list of lists"""


def pascal_triangle(n):
    """this model is for creating a function
    pascal_triangle that returns a list of lists"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        temp = [0] + triangle[-1] + [0]
        row = []
        for i in range(len(triangle[-1]) + 1):
            row.append(temp[i] + temp[i + 1])
        triangle.append(row)
    return triangle
