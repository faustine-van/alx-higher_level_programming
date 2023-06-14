#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = [[x for x in row]for row in matrix]
    sqrt = map(lambda row: [x**2 for x in row], matrix1)
    square = list(sqrt)
    return square
