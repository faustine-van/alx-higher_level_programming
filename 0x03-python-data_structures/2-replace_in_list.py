#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for a in range(len(my_list)):
        if idx == a:
            my_list[idx] = element
    return my_list
