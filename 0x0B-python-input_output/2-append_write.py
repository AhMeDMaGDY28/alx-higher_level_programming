#!/usr/bin/python3
"""This module defines a file-abending function."""


def append_write(filename="", text=""):
    """Abends a string to a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(f"{text}")
