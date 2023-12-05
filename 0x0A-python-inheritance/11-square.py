#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """Reprsent base geometry based on 6-base_geometry.py"""

    def area(self):
        """a function that is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validet the value and checks for the errors.

        Args:
            name : The name of the parameter and must be str.
            value : The parameter to validate in type of int.
        Raises:
            If value is not an integer TypeError must be an integer,
            If value is not greater than 0 ValueError must be greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
