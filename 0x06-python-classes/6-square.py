#!/usr/bin/python3

"""This module is square class"""


class Square:

    """This square class that defined by Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if (
            not isinstance(value, tuple)
            and not len(value) == 2
            and not all(isinstance(x, int) and x > 0 for x in value)
           ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This square class that defined by Square"""
        return self.size ** 2

    def my_print(self):
        """This square class that defined by Square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
