#!/usr/bin/python3
"""Creating a class called MyList"""


class MyList(list):
    """ Class that inherit the attribute from class list 

    Args:
        list: Class list


    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        SortList = self.copy()
        SortList.sort()
        print(SortList)
