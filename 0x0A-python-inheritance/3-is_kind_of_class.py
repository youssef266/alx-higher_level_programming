#!/usr/bin/python3
"""this model is to know if the object is instance
or not
"""


def is_kind_of_class(obj, a_class):
    """a function that knowes if the object is instance
    Args:
        obj: the specific object
        a_class: the class that inhert from
    Return:
        returns True if the object is an instance of,
        or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False