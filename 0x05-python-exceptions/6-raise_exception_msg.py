#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not isinstance(message, str):
        raise NameError(message)
