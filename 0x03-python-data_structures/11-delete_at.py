#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list):
        return my_list
    for a in my_list:
        if idx == a:
            del my_list[idx]
    return my_list
