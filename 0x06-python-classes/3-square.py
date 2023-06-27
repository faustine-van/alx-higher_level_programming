#!/usr/bin/python3

"""This module  class Square that defines a square"""


class Square:
    """This Square class that defines a square"""
    def __init__(self, size=0):
        """Initialize the square with the given size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """function create area of square"""
        area = self.__size ** 2
        return area
