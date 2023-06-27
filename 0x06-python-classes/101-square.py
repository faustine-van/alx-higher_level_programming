#!/usr/bin/python3

"""This module is square class"""


class Square:

    """This square class that defined by Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set size setter method"""
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
        """set position using setter method"""
        self.__position = value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This square class that defined by Square"""
        area = self.size ** 2
        return area

    def my_print(self):
        """This square class that defined by Square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        if self.size == 0:
            return "\n"

        square = ""
        for _ in range(self.position[1]):
            square += "\n"

        for _ in range(self.size):
            square += " " * self.position[0] + "#" * self.size + "\n"

        return square.strip()
