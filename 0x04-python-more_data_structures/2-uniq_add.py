#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for a in set(my_list):
        res += a
    return res
