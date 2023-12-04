#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """a function that adds a new attribute to an
    object if it’s possible

    Args:
        obj : The object to add an attribute to could be any tybe.
        att : The name of the attribute to add to obj string.
        value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added
        the typeeroor is can't add new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
