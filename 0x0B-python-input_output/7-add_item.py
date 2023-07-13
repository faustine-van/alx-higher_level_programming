#!/usr/bin/python3
import sys
"""adds all arguments to a Python list, and then save them to a file"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
argc = len(sys.argv)
new_list = []

for i in range(1, argc):
    new_list.append(args[i])
save_to_json_file(new_list, "add_item.json")
