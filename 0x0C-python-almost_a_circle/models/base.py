#!/usr/bin/python3
"""this model is for class name base that is
the Base to Square and Rectangle
"""


class Base:
    """this is a Base calss
    Private Class Attributes:
        __nb_objects: an private for type int
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """this init function to the att id
        Args:
            id: indentify the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
