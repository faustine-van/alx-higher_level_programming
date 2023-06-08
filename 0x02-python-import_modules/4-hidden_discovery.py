#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden_file = dir(hidden_4)

    for name in hidden_file:
        if name[1] != '_':
            print(name)
