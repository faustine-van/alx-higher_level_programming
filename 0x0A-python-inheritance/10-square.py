#!/usr/bin/python3
"""Module create empyty class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ subclass Square that inherits from Rectangle
    """

    def __init__(self, size):
        """ initialize width ang height
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ set area
        """
        return self.__size * self.__size
