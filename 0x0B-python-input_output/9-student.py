#!/usr/bin/python3
"""thei model is for class student that define a student
by first_name, last_name and age"""


class Student:
    """class Student that defines a student
    by first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
