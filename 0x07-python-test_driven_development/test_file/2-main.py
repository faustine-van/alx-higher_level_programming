#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided([[1, 3, 9], [2, 5, 6],[4,7]], 6))
print(matrix)

print(matrix_divided(['e',[4, 5, 6]], 2))