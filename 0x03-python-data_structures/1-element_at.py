#!/usr/bin/python3

def element_at(my_list, idx):
    for a in range(len(my_list)):
        if idx < 0:
            return "None"
        if idx > len(my_list):
            return "None"
        if (a == idx):
            return my_list[idx]
