#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = [a * b for (a, b) in my_list]
    res1 = [b[1] for b in my_list]
    sum1 = 0
    sum2 = 0
    average = 0
    for a in res:
        sum1 += a
    for b in res1:
        sum2 += b

    average = sum1 / sum2
    return average
