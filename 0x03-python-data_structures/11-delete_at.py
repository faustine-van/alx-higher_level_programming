#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list):
        return my_list
    if idx < 0:
        return my_list
# use enumerate to access both element and index
    for a, x in enumerate(my_list):
        if a == idx:
            del my_list[idx]
    return my_list
