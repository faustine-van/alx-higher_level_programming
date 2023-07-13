#!/usr/bin/python3
import sys
"""adds all arguments to a Python list, and then save them to a file"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
argc = len(sys.argv)
new_list = []

try:
    # to loads in order to be able to append to the list
    existing_list = load_from_json_file("add_item.json")

    # adds the specified list elements to the end of the current list.
    new_list.extend(existing_list)
except FileNotFoundError: # this create file if doesn't exist
    pass

for i in range(1, argc):
    new_list.append(args[i])
# and the convert the into json
save_to_json_file(new_list, "add_item.json")
