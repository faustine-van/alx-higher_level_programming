#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arc = len(sys.argv) - 1
    args = sys.argv
    res = 0
    if arc >= 1:
        for a in range(arc):
            res += int(args[a + 1])
    print(res)
