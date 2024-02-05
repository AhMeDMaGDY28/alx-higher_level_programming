#!/usr/bin/python3
"""
this is a class MyList that inherits from list
"""


class MyList(list):
    "a class which inherits from list"
    def print_sorted(self):
        "a func to print a sorted list"
        print(sorted(self))
