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

    def save_to_file(cls, list_objs):
        """save the file"""
        file_name = cls.__name__ + ".json"
        dict_list = []
        if list_objs is not None:
            for instance in list_objs:
                dict_list.append(instance.to_dictionary())
        with open(file_name, 'w', encoding='utf-8') as file_a:
            file_a.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """loads an object form JSON"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(2, 2)
        elif cls is Square:
            obj = Square(4)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """loads JSON from file and convert it to object"""
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = cls.__name__ + ".json"
        with open(file_name, encoding='utf-8') as file_a:
            if cls is Rectangle:
                return [Rectangle.create(**dictionary) for dictionary
                        in Rectangle.from_json_string(file_a.read())]
            if cls is Square:
                return [Square.create(**dictionary) for dictionary
                        in Square.from_json_string(file_a.read())]
