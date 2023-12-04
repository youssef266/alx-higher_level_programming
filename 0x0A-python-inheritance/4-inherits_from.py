#!/usr/bin/python3
"""this model is to checks if the object instance or not"""


def inherits_from(obj, a_class):
    """the function check if the object instance or not
    Args:
        obj: the specific object
        a_class: the class that inhert from
    Return:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
