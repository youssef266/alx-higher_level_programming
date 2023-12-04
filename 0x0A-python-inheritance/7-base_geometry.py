#!/usr/bin/python3
"""this model is for  a class BaseGeometry
based on 6-base_geometry.py
"""


class BaseGeometry:
    """this class based on 6-base_geometry.py"""
    def area(self):
        """an function"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """a function that validates the value
        Args:
            name: name in type str
            value: the value of this name
        Return:
            TypeError if the vlaue is not integer,
            ValueError if the value less than or equal 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer")
        elif value <= 0:
            raise ValueError("{} must be greater than 0")
