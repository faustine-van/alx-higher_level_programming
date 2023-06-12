#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list):
        return my_list
    if idx < 0:
        return my_list
# use enumerate to access both element and index
# for a, x in enumerate(my_list): like this
    for a in range(len(my_list)):
        if idx == a:
            del my_list[idx]
    return my_list
