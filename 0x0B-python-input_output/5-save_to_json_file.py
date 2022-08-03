#!/usr/bin/python3
"""
module that contain function that saves Json string into a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file
    by a JSON representation


    Args:
       my_obj: The Object to be saved
       filename: The file it should be saved to

    Raise:
        Exception: when the file can't be opened

    """

    with open(filename, 'w', encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
