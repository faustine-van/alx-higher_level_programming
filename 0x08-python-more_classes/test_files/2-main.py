#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 0
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 0
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

try:
    my_rectangle.width = 1.3
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)

print("--")

try:
    my_rectangle.width = "her"
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)

