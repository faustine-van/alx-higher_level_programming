#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    roman = roman_string
    for i in range(len(roman)):
        if i < len(roman) - 1 and val[roman[i]] < val[roman[i + 1]]:
            total -= val[roman_string[i]]
        else:
            total += val[roman_string[i]]
    return total
