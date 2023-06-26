#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        res = num1 / num2
        return res
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
