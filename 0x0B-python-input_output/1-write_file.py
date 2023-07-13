#!/usr/bin/python3
"""Module read text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of
    characters written
    """
    with open(filename, 'w', encoding="utf-8") as filename:
        fd = filename.write(text)
    return fd
