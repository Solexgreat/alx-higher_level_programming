#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_listd = []
    if idx < 0 :
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    for i in my_list:
       my_listd.append(i)
    my_listd[idx] = element
    return (my_listd)
