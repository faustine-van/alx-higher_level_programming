#!/usr/bin/python3
"""Module create class"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """ area() method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """ def integer_validator() method

            args:
                 name: name
                 value: value
            Raises:
                  - if value is not an integer
                  - if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """ subclass Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ initialize width ang height
            args:
                width: width of rectangle
                height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
