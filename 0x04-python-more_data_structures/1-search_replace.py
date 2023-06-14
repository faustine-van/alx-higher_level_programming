#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [x for x in my_list]
    for a, x in enumerate(new_list):
        if new_list[a] == search:
            new_list[a] = replace
    return new_list
