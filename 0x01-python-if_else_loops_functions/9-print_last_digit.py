#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    a = number % 10
    print(a, end="")

# function return allows the caller to utilize the result if needed.
    return a
