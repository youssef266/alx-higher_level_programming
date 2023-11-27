#!/usr/bin/python3

"""this model for prints a text
with two line after it 
"""


def text_indentation(text):
    """text must be str otherwise print typeerror
    Args:
        - text: str of the text 
    """
    delimitors = '.:?'

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for delim in delimitors:
        text = (delim + "\n\n").join(
            [l.strip(" ") for l in text.split(delim)])
        
    print(text, end='')
