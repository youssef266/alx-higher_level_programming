#!/usr/bin/python3
"""this model prints <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    Args:
    - firstname: my first name
    - lastname: my last name
    """

    fname_error_m = 'first_name must be a string'
    lname_error_m = 'last_name must be a string'

    if not isinstance(first_name, str):
        raise TypeError(fname_error_m)
    
    if not isinstance(last_name, str):
        raise TypeError(lname_error_m)
    
    print(f'My name is {first_name} {last_name}')
