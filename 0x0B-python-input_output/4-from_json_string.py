#!/usr/bin/python3
"""
module that contain function that deserilize Json string to Python obj
"""
import json


def from_json_string(my_str):
    """
    Function that convert JSON string into python object

    Args:
       my_str: The string

    Raise:
       Exception: when the file can't be opened

    """

    return json.loads(my_str)
