#!/usr/bin/python3
"""Module"""
import json


def class_to_json(obj):
    """class to json"""
    if hasattr(obj, "jsonEnc"):
        return obj.jsonEnc
    else:
        return obj.__dict__
