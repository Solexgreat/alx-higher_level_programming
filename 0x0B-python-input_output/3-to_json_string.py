#!usr/bin/python3
"""
module that contain function that serilize Python obj to 
a Json string 
"""
import json


def to_json_string(my_obj):
    """
    Function that convert a python object to a JSON string

    Args:
        my_obj: The python object

    Raise:
         Exception: when the file can't be opened

    """

    return json.dumps(my_obj)
