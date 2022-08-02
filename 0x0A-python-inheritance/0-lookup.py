#!/usr/bin/python3

def lookup(obj):
    """
    The function return the list of method in the obj 

    Args:
    obj: instance of a class

    Return:
    List of method
    """

    return (dir(obj))
