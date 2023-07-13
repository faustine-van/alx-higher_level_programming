#!/usr/bin/python3
"""Module"""


class Student:
    """define student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a diction represantation of a Student instance"""
        json_dict = {}
        for key, val in self.__dict__.items():
            if isinstance(val, (list, str, dict, int, bool)):
                json_dict[key] = val
        return json_dict
