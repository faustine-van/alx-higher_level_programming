#!/usr/bin/python3
"""Module prevents the user from dynamically creating new attributes"""


class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(
                f"'{__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)
