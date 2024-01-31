#!/usr/bin/python3
"""
say_my_name function

This function prints a person's name based on the provided
first name and last name.

Parameters:
- first_name (str): The first name of the person.
- last_name (str, optional): The last name of the person.
Defaults to an empty string if not provided.

Raises:
- TypeError: If either first_name or last_name is not a string.

Returns:
- None
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the provided first and last name.

    Parameters:
    - first_name (str): The first name of the person.
    - last_name (str, optional): The last name of the person.
    Defaults to an empty string if not provided.

    Raises:
    - TypeError: If either first_name or last_name is not a string.

    Returns:
    - None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
