#!/usr/bin/python3
"""module"""


def add_attribute(a, name, value):
    """function add new attributes"""
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a, name, value)  # a.__dict__[name] = value
