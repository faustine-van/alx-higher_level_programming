#!/usr/bin/python3
"""Module append string to the file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
       returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as filename:
        file = filename.write(text)
    return file
