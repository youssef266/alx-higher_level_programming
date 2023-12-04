#!/usr/bin/python3
"""a class that def rectangle based on 7-base_geometry and inhert from
BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle and inhert from BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        with width and hight.
        super class
        Args:
            width : The width of the new Rectangle with type of int.
            height : The height of the new Rectangle with type of int.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
