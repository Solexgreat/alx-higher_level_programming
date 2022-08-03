#!/usr/bin/python3
"""
module that contain function that appends to a file 
"""


def append_write(filename="", text=""):
    """Function that append to a file

    Args:
        filename: filename
        text: text to be added

    Raise:
        Exception: when the file can't be opened

    """

    with open(filename, 'a', encoding="utf-8") as myfile:
        return myfile.write(text)
