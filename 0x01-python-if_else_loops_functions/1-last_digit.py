#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
b = int(number / 10)
a = number - (10 * b)
if a > 5:
    print("Last digit of", number, "is", a, "and is greater than 5")
elif a == 0:
    print("Last digit of", number, "is", a, "and is 0")
elif a < 6 and not 0:
    print("Last digit of", number, "is", a, "and is less than 6 and not 0")
