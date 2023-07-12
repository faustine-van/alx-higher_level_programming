#!/usr/bin/python3
"""Module create empyty class"""


class BaseGeometry:
    """ empty class BaseGeometry
    """
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
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ set area
        """
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height)


class Square(Rectangle):

    """ subclass Square that inherits from Rectangle
    """

    def __init__(self, size):
        """ initialize size
        """
        self.__size = size

        self.integer_validator("size", self.__size)

    def area(self):
        """ set area
        """
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__size, self.__size)
