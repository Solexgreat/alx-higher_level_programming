#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list) - 1
    if idx < 0 and idx > lenght:
        return None
    for i in range(len(my_list)):
        if i == idx:   
            return (my_list[i])
