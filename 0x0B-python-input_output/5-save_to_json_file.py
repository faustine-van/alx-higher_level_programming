#!/usr/bin/python3
"""Module"""
import json


def save_to_json_file(my_obj, filename):
    """write an object Python data structure using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as file:
        json_data = json.dumps(my_obj)
        file.write(json_data + '\n')
