#!/usr/bin/python3
"""Module  create class Rectangle that defines a rectangle
"""


class Rectangle:
    """defines a rectangle """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        """return area of rectangle"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """return perimeter of rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        perimeter = (self.width + self.height) * 2
        return perimeter
