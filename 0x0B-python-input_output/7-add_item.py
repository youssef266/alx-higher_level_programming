#!/usr/bin/python3
"""this model is for adds all arguments to a Python list
and then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
loade_form_json = __import__('6-load_from_json_file').load_from_json_file


args = list(sys.argv[1:])

try:
    items = loade_form_json("add_item.json")
except Exception:
    items = []
finally:
    items.extend(args)
    save_to_json_file(items, "add_item.json")
