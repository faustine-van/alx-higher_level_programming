#!/usr/bin/python3
"""create class from int"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
