#!/usr/bin/python3
def max_integer(my_list=[]):
    num = my_list[0]
    for a in my_list:
        if a > num:
            num = a
    return num
