#!/usr/bin/python3

"""Module multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):

    """function multiplies 2 matrices by using the module NumPy
    """

    a = numpy.array(m_a)
    b = numpy.array(m_b)

    res = numpy.matmul(a, b)

    return res
