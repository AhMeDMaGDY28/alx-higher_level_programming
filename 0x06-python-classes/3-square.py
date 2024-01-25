#!/usr/bin/python3
"""this is docemntion for square"""


class Square:
    """square size control"""
    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
    """this function to measure the area of the square."""
    def area(self):
        return self.__size**2
