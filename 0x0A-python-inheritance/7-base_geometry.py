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
