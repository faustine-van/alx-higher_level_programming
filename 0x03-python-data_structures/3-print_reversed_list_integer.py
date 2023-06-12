#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for a in my_list[::-1]:  # or for a in range(len(my_list)):
        print("{:d}".format(a))  # or print("{}".format(my_list[-a - 1])
