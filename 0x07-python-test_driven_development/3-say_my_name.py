#!/usr/bin/python3
"""
This module define function that print Name
"""


def say_my_name(first_name, last_name=""):
    """ print the first name and the last name
    Arguments:
        first_name: first name
        last_name: last name
    Raises:
        if first_name must be a string or last_name must be a string
    print the name

    Usage examples:
    input: say_my_name("John", "Smith")
    output: My name is John Smith

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
