#!/usr/bin/python3
"""Defines an object attribute lookup function"""

def lookup(obj):
    """Function return the list of methods in the objects

    Args:
        obj: instance of a class

    Return:
        List of methods

    """

    return (dir(obj))
