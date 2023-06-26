#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        res = None
        try:
            if x >= len(my_list_1) or x >= len(my_list_2):
                raise IndexError("out of range")
            a = my_list_1[x]
            b = my_list_2[x]
            if not isinstance(a, (int, float)):
                raise TypeError("wrong type")
            if not isinstance(b, (int, float)):
                raise TypeError("wrong type")
            if b == 0:
                raise ZeroDivisionError("division by 0")
            res = a / b
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        finally:
            new_list.append(res)
    return new_list
