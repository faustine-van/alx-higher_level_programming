#!/usr/bin/python3

"""This module class Square that defines a square"""


class Square:
    """This Square class that defines a square"""
    def __init__(self, size=0):
        self.__size = size  # Private instance attribute
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
