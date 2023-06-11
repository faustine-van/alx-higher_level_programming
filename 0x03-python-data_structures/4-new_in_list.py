#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = [x for x in my_list]
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for a in range(len(new_list)):
        if idx == a:
            new_list[idx] = element
    return new_list
