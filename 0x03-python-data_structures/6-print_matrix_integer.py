#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for j in a:
            print("{}".format(j), end=" ")
        print()
