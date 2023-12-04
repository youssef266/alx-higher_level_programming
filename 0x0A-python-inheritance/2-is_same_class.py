#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """a function that cheak if the
    object instance
    Args:
        obj: is the object
        a_class: is the specific class
    Return:
        true if the object exactly instance of
        the specified classo otherwise - false
    """
    if type(obj) == a_class:
        return True
    return False
