#!/usr/bin/python3
"""Module  create class Rectangle that defines a rectangle
"""


class Rectangle:
    """defines a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """set width  of rectangle """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle  """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
