#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""

import sys
import json
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
argc = len(sys.argv)
new_list = []

if exists("add_item.json"):
    # to loads in order to be able to append to the list
    data_list = load_from_json_file("add_item.json")

else:
    data_list = []

# adds the specified list elements to the end of the current list.
# new_list.extend(existing_list)
# except FileNotFoundError:  # This create file if doesn't exist
#    pass

for i in range(1, argc):
    data_list.append(args[i])

# Save the updated list to "add_item.json"
save_to_json_file(data_list, "add_item.json")
