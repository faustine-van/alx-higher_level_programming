#!/usr/bin/python3

for a in range(9):
    for x in range(a + 1, 10):
        if x != a:
            print("{}{}".format(a, x), end="")
            if a != 8 and a != 9:
                print(", ", end="")
            else:
                print()
