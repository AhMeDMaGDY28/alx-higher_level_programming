#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text filename"""
    file = open(str(filename), 'r', encoding="utf-8")
    print(file.read(), end="")
