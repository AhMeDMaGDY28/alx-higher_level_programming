#!/usr/bin/python3
"""this is docemntion for square"""


class Square:
    """square size control"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """this function to measure the area of the square."""
    def area(self):
        return self.__size**2
    """this is size function"""
    @property
    def size(self):
        return self.__size
    """i dont know what i call tis """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """this is this print for priniting the square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
