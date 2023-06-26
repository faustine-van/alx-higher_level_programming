#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    count = 0
    while a < x:
        try:
            print(my_list[a], end="")
            a += 1
            count += 1
        except IndexError:
            break
    print()
    return a
