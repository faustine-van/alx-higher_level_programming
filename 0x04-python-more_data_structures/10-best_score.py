#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_str = None
    max_val = float('-inf')
    for key, val in set(a_dictionary.items()):
        values = int(val)
        if (values > max_val):
            max_val = values
            max_str = key
    return max_str
