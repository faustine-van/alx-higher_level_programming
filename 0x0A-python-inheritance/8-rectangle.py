#!/usr/bin/python3
"""Module create class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ subclass Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ initialize width ang height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
