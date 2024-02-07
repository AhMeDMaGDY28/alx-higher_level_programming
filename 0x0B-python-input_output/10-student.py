#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """init a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dict"""
        dict = {}
        if type(attrs) is list:
            for i in attrs:
                for key, value in self.__dict__.items():
                    if i == key:
                        dict[i] = value
            return dict
        return self.__dict__
