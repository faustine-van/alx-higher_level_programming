#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for r, j in enumerate(a):
            print("{:d}".format(j), end="")
            if r != len(a) - 1:
                print(" ", end="")
        print()
