#!/usr/bin/python3
"""
module that contain function that add argument to a python
list and save them to a json file
"""
import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


mylist = []

if os.path.exists("add_item.json"):
    load_file("add_item.json")

for i in range(len(sys.argv - 1)):
    if i != 0:
        mylist.append(sys.argv[i])

save_file(mylist, "add_item.json")
