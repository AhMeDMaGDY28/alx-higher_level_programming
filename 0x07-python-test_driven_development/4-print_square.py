#!/usr/bin/python3
"""
a model to print square from the char '#'
"""


def print_square(size):
    "function which prints a square with the size of size variable"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        return
    elif size == 1:
        print("#")
    else:
        for i in range(0, size):
            for x in range(0, size):
                print("#", end='')
            print()
