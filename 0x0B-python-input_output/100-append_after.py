#!/usr/bin/python3
"""Module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text into a file"""

    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    with open(filename, 'w', encoding="utf-8") as file:
        for line in lines:  # iterate through lines
            file.write(line)  # write existing line if search string is not
            if search_string in line:
                file.write(new_string)
