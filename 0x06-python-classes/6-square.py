#!/usr/bin/python3

"""This module is square class"""


class Square:

    """This square class that defined by Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not value[0] > 0 or not value[1]:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """public instance method that  calculate area with size argumebt"""
        area = self.__size ** 2
        return area

    def my_print(self):
        """print the #  and space with size and position"""
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()
