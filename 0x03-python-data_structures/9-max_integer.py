#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return none
    x = 0
    for i in my_list:
        x = i if i > x else x
    return x
