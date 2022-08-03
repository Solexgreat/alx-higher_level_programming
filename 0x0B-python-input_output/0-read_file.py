#!/usr/bin/python3
"""module that contain function that reads from a file
"""


def read_file(filename=""):
    """Function that append to a file

       Args:
        filename: filename

    Raise:
        Exception: when the file can't be open

    """

    with open(filename, encoding="utf-8") as myfile:
        filee = myfile.read()
        print(filee, end='')
