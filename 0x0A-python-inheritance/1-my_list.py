#!/usr/bin/python3
"""this model is to create a class name my list"""


class MyList(list):
    """print all the list but sorted"""
    def print_sorted(self):
        """print all the list sorted"""
        print(sorted(self))
