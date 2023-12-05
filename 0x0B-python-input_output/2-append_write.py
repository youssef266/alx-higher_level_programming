#!/usr/bin/python3
"""this model is to append a text file"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
