#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """init a new student"""
        slef.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the dict"""
        return self.__dict__
