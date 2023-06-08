#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arc = len(sys.argv) - 1
    args = sys.argv
    print("{} {}".format(
        arc,
        "arguments." if arc == 0 else "argument:" if arc == 1 else "arguments:"
        ))
    if arc >= 1:
        for a in range(arc):
            print("{}: {}".format(a + 1, args[a + 1]))
