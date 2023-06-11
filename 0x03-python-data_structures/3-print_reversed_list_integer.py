#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for a in range(len(my_list)):
        print("{:d}".format(my_list[-a - 1]))   # try [::-1]
