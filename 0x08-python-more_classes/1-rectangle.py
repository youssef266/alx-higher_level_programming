#!/usr/bin/python3
"""this model is for Rectangle class"""


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            width: width of the rectangle with type int
            height: height of the rectangle with type int
    """
    def __init__(self, width=0, height=0):
        """
            initialises the instances
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
            width must be >= 0
            and must be an int
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
            getter function for private attribute width
            Retruns: width
            and gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for private attribute width
            Args:
                value: new width value for type int
            if it is not instance handle typeerror and valueerror
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for private attribute height
            Returns: height
            handling all the hight exceptions
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
            Args:
                value (int): new height value
            handling all the hight exceptions
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
