#!/usr/bin/python3

"""This module to take  python bytecode to python class called MagicClass"""

import math


class MagicClass:
    """This class is for calculate area and circumference."""

    def __init__(self, radius):
        """Initialize radius

           Argument:
               radius : which float or int
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area of circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate circumference of circle"""
        return (2 * math.pi * self.__radius)
