#!/usr/bin/python3
"""Module define first class Base"""
import json


class Base:
    """Module define first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w', encode="utf-8") as file:
           file.write(json_str)

    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json_string
