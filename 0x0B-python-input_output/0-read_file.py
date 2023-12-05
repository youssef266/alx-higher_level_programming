#!/usr/bin/python3
"""Contain a single function that read files"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
