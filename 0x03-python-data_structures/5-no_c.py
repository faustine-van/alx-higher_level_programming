#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for a in my_string:
        if a == "c" or a == "C":  # or a.lower() == 'c'
            continue
        res += a
    return res


"""def no_c(my_string):
    result = ''.join([char for char in my_string if char.lower() != 'c'])
    return result
"""
