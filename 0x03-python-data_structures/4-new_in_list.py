#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_listd = my_list[:]
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    my_listd[idx] = element

    return (my_listd)
