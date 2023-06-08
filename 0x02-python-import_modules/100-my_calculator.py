#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    arc = len(sys.argv)
    args = sys.argv
    res = 0
    if arc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    op = args[2]
    b = int(args[3])
    if op == '+':
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, res))
