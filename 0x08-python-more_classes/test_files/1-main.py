#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
print("--")
try:
    my_rectangle.width = 0
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

except Exception as e:
    print(e)
print("--")
try:
    my_rectangle.width = 3
    my_rectangle.height = "five"
    print(my_rectangle.__dict__)

except Exception as e:
    print(e)
print("--")
try:
    my_rectangle.width = 1.5
    my_rectangle.height = 8
    print(my_rectangle.__dict__)

except Exception as e:
    print(e)
print("--")

try:
    my_rectangle.width = -3
    my_rectangle.height = "five"
    print(my_rectangle.__dict__)

except Exception as e:
    print(e)
