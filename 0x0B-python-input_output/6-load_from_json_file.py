#!/usr/bin/python3
"""this module is for creating an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file
    by loading it"""
    with open(filename, 'r') as f:
        return json.load(f)
