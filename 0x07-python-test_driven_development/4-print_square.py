#!/usr/bin/python3

"""This model prints squares"""


def print_square(size):
    """print squer by using #
    that make the shape of square
    Args:
       - size
    """

    size_error_m1 = 'size must be an integer'
    size_error_m2 = 'size must be >= 0'
    if not isinstance(size, int):
        raise TypeError(size_error_m1)
    
    if size < 0:
        raise ValueError(size_error_m2)
    
    if size >= 0:
        for i in range(size):
            print("#" * size)
