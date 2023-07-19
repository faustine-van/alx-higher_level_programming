#!/usr/bin/python3
"""module inheritance class Rectanle"""
from models.base import Base


class Rectangle(Base):
    """class Rectanle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """class Rectanle"""
        return self.__width

    @width.setter
    def width(self, value):
        """class Rectanle"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """class Rectanle"""
        return self.__height

    @height.setter
    def height(self, value):
        """class Rectanle"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """y attribute"""
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y Rectanle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setting y"""
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")

    def area(self):
        """area of Rectanle"""
        return self.__width * self.__height

    def display(self):
        """display Rectanle"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """class Rectanle"""
        return "[{}] ({}) {}/{} - {}/{}".format(
          __class__.__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """many argument"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, value in enumerate(args):  # for i,value in zip(attrs, args):
            if i < len(attrs):
                setattr(self, attrs[i], value)  # setattr(self, i, value)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to dicitionary represenattion"""
        return {
             "id": self.id,
             "width": self.width,
             "height": self.height,
             "x": self.x,
             "y": self.y
             }
