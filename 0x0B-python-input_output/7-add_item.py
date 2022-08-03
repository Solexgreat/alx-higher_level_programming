#!/usr/bin/python3
"""
module that contain function that add argument to a python
list and save them to a json file
"""
import sys
import os
import save_to_json_file from 5-save_to_json_file.py
import load_from_json_file from 6-load_from_json_file.py


mylist = []

if os.path.exists("add_item.json"):
    load_from_json_file("add_item.json")

for i in range(len(sys.argv - 1)):
    if i != 0:
        mylist.append(sys.argv[i])

save_to_json_file(mylist, "add_item.json")
