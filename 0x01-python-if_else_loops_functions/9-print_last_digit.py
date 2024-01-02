#!/usr/bin/python3
def print_last_digit(num):
    x = abs(num) % 10
    print('{}'.format(x), end="")
    return x
