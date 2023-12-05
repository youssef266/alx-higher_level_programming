#!/usr/bin/python3
"""model that returne a josn represented by an objedt str"""
import json


def to_json_string(my_obj):
    """returns the json represtion a object for type string"""
    json_object = json.dumps(my_obj)
    return json_object
