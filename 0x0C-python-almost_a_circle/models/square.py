#!/usr/bin/python3
"""module inheritance class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value  # option

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__, self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """updated"""
        attrs = ["id", "size", "x", "y"]
        for i, val in enumerate(args):
            if i < len(args):
                setattr(self, attrs[i], val)

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
