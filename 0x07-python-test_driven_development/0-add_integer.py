#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """define for an adding function

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    Return:
        result for adding a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
