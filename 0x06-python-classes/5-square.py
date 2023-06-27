#!/usr/bin/python3

"""This module  class Square that defines a square"""


class Square:
    """This Square class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """function create area of square"""
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print()
        for _ in range(self.size):
            for _ in range(self.size):
                print("#", end="")
            print()
