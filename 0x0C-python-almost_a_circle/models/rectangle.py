#!/usr/bin/python3
"""this model is for Rectangle class
that inherits from Base calss
"""
from models.base import Base


class Rectangle(Base):
    """this class is for Rectangle that
    inherits some att from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """handling the the rectangle
        Args:
            width: is for the width of the rectangle
            height: is for handling the height of the rectangle
            x:an att for type int private
            y: an att for type int private
        Handling Exiptions:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """is gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
