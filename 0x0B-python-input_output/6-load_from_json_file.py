#!/usr/bin/python3
"""a func  that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as file:
        return json.load(file)
