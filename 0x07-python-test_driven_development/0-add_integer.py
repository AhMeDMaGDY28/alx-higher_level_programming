#!/usr/bin/python3
"""

This is a function which adds two numbers.

"""


def add_integer(a, b=98):
    """
    Adds two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
