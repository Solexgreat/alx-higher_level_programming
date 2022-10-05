#!/usr/bin/python3
def search_replace(my_list, search, replace):
    num = (lambda x: x if x != search else replace)
    return list(map(num, my_list))
