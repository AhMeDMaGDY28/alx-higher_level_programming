#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    x = 0
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        for i in my_list:
            if x == idx:
                my_list.remove(i)
            x += 1
        return my_list
