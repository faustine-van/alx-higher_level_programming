#!/usr/bin/python3

"""Module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):

    """multplies two matrix

       Args:
            m_a:matrix one
            m_b:matrix two
       Returns:
           result of multiplies 2 matrices
    """
    # check if list m_a or m_b is empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # If m_a and m_b can’t be multiplied/Checking matrix dimensions:
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # check list m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check a list of list  or list is list of integer or float and check size
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError(
                            "m_a should contain only integers or floats"
                             )
    for row1 in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        if not isinstance(row1, list):
            raise TypeError("m_b must be a list of lists")
            for k in row1:
                if not isinstance(k, (int, float)):
                    raise TypeError(
                            "m_b should contain only integers or floats"
                            )
# create empty result list
    res = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for a in range(len(m_a)):
        for b in range(len(m_b[0])):
            for i in range(len(m_b)):
                res[a][b] += m_a[a][i] * m_b[i][b]

    return res
