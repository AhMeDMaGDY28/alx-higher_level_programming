#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text filename"""
    with open(str(filename), encoding="utf-8") as file:
        print("{}".format(file.read()), end="")
        file.close()
