#!/usr/bin/python3
"""Defines an object attribute lookup function"""

def lookup(obj):
    """The function return the list of method in the objects

    Args:
        obj: instance of a class

    Return:
        List of method

    """

    return (dir(obj))
