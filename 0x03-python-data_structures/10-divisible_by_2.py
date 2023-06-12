#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [a % 2 == 0 for a in my_list if True]
    return new_list
