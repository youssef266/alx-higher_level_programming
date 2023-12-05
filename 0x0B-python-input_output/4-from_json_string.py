#!/usr/bin/python3
"""a model that contain a single function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string"""
    json_loaded = json.loads(my_str)
    return json_loaded
