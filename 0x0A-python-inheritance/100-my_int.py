#!/usr/bin/python3
"""Define a Clss MyInt that inherits from Int"""


class MyInt(int):
    """ Invert int operators == and !="""

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
