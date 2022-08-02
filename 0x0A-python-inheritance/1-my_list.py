#!/usr/bin/python3
"""Creating a class called MyList"""

class MyList(list):
    """ Class that inherit the attribute from class list 

    Args:
        list: Class list
    """
    def print_sorted(self):
        SortList = []
        for i in self:
            SortList.append(i)
        SortList.sort
        print("{}".format(SortList))
