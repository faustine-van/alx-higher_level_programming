#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for a in range(len(my_list)):
        if (all(isinstance(elem, int) for elem in my_list)):
            print("{:d}".format(my_list[a]))
# instead of instance use print("{:d}".format(my_list[a]))
