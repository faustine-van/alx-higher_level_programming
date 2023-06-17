#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Find the key associated with the value 'value2'
    key_to_del = [key for key, val in a_dictionary.items() if val == value]
    for key in key_to_del:
        del a_dictionary[key]

    return a_dictionary
