#!/usr/bin/python3
"""this module defines a class Student depending on 10-student"""


class Student:
    """class Student that defines a student
    by first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        dictionary = self.__dict__
        if attrs is None:
            return dictionary

        d = {k: v for k, v in dictionary.items() if k in attrs}
        return d
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        self.__dict__.update(json)
