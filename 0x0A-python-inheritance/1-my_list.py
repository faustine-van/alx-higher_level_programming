#!/usr/bin/python3
"""module"""


class MyList(list):
    """class MyList inherited from list"""
    def print_sorted(self):
        new_list = []
        for i in self:
            new_list.append(i)
        print(sorted(new_list))
