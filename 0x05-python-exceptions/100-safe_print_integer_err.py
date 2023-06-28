#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        message_error = "Exception: " + str(e)
        print(message_error, file=sys.stderr)
        return False
