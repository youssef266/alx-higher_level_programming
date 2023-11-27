#!/usr/bin/python3
"""
This program divide a matrix of by a divisor
Definition:
- matrix: list of list
- numbers: float or int
- divisor: float or int
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with the elements divided by a int or float
    Args:
      - matrix (list of list)
      - div (int or float)
    The lists inside of the matrix must be of the same size
    """
    new_m = []
    error_message = 'matrix must be a matrix (list of lists) of integers/floats'

    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    if not isinstance(matrix, list):
        raise TypeError(error_message)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if len(matrix) == 0:
        return new_m

    elements = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_message)

        if len(row) != elements:
            raise TypeError('Each row of the matrix must have the same size')

        for num in row:
            if (type(num) not in [int, float]):
                raise TypeError(error_message)

        new_m.append(list(map(lambda num: round(num / div, 2), row)))

    return new_m
