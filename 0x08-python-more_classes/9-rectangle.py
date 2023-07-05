#!/usr/bin/python3
"""

This module is composed by a class that defines a Rectangle


"""


class Rectangle:
    """defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ method that returns the value of the width

        Returns:
            rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """return perimeter of rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        perimeter = (self.width + self.height) * 2
        return perimeter

    def __str__(self):
        """print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for _ in range(self.height - 1):
            rectangle += self.print_symbol * self.width + "\n"
        rectangle += self.print_symbol * self.width
        return rectangle

    def __repr__(self):
        """return a string representation of the rectangl"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Method that prints a message when the instance is deleted


        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the bigger Rectangle

        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        Raises:
            TypeError: when some argument passed is not
            an instance of the Rectangle class

        Returns:
            The bigger Rectangle


        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
