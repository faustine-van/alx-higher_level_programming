#!/usr/bin/python3
"""
This module  prints a square with the character #.

"""


def print_square(size):
    """ function  prints a square with the character #.
    Arguments:
        size: the size length of the square
    Raises:
        case1 - size is not integer
        case2 - size is less than 0
    print square with #

    Usage examples:
    >>>print_square(4)
    ####
    ####
    ####
    ####
    >>>print_square(1)
    size must be >= 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
