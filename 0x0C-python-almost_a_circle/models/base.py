#!/usr/bin/python3
"""this defines a class named base"""
import json


class Base:
    """this is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """hello world"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)
