#!/usr/bin/python3

def add_attribute(a, name, value):
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a, name, value)  # a.__dict__[name] = value
