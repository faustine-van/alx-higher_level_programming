#!/usr/bin/python3
"""this module to take  python bytecode to
   python class called MagicClass
"""
import math


class MagicClass:
    """this class is for calculate area and circumference"""
    def __init__(self, radius):
        """initialize radius"""
        self.MagicClass__radius = 0
        if type(radius) is not int() or type(radius) is not float():
            raise TypeError("radius must be a number")
        else:
            self.MagicClass__radius = radius

    def area(self):
        """ calculate area of circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """calculate circumference of circle"""
        return 2 * math.pi * self._MagicClass__radius
