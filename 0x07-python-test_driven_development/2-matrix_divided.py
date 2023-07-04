#!/usr/bin/python3
"""
This module that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix..
    Arguments:

        matrix: matrix to be used
        div: used to devide to list in matrix

    Returns:
        New matrix with divided elements.

    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in row:
            if not isinstance(y, (int, float)):
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                   )

        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((x / div), 2) for x in row]for row in matrix]
    return new_matrix
