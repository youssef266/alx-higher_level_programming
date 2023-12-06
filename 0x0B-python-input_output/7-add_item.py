#!/usr/bin/python3
"""Handles file input and saves to file"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argv.pop(0)
try:
    my_list = load_from_json_file("add_item.json")
except  Exception:
    my_list = []
    save_to_json_file(my_list + argv, "add_item.json")

except FileNotFoundError:
    save_to_json_file(argv, "add_item.json")
