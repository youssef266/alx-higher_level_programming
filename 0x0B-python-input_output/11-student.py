#!/usr/bin/python3
"""Class defination of student"""


class Student:
    """Defines a student class 
    with first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        """Initializes instance data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves the dictionary representation 
            of  studentfor the list of attributes 
            if attrs is a list
        """
        dictionary = self.__dict__
        if attrs is None:
            return dictionary

        d = {k: v for k, v in dictionary.items() if k in attrs}
        return d

    def reload_from_json(self, json):
        """
            Replaces all attributes of the Student instance
            and then updates
        """
        self.__dict__.update(json)
