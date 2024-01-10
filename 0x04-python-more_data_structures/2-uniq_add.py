#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new_list = list(set(new_list))
    sum = 0
    for i in new_list:
        sum += i
    return (sum)
