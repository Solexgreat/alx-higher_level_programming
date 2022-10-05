#!/usr/bin/python3
"""
module that contain function that load from a JSON file to
a python object
"""
import json


def load_from_json_file(filename):
    """Function that load from a JSON file to
       a python object

    Args:
       filename: The JSON file

    Raise:
       Exception: when the file can't be opened

    """

    with open(filename, 'r', encoding="utf-8") as myfile:
        return json.load(myfile)
