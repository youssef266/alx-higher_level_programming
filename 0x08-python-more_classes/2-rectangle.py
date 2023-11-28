#!/usr/bin/python3
"""This program define a class Rectangle with private attributes and methods"""


class Rectangle():
    """
    A Rectangle Class with the private instance attributes width and height
    and public methods
    and handling of all exceptions
    """

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width : int for input width default 0
            - heigth : int for input width default 0
        """
        self.height = height
        self.width = width

    def area(self):
        """Calculate the area of a Rectangle
        width * heigt
        """
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle
        and return 0
        and then add width to hight
        """
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """Getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Getter of the property value
          Args:
            - value: int new value of width
        handling of all exceptions
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Getter of the property height
        intgret self
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Getter of the property value
          Args:
            - value: int new value 
        handling of all exceptions
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
