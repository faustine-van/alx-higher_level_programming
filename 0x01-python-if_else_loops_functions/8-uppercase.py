#!/usr/bin/python3

def uppercase(str):
    for a in str:
        b = ord(a)
        if b >= 97 and b <= 122:
            c = chr(b - 32)
        else:
            c = a
        print("{}".format(c), end='')
    print()
