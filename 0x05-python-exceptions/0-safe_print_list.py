#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    k = 0
    for i in my_list:
        if k < x:
            print("{}".format(i), end='')
            a += 1
        k += 1
    print('')
    return a
