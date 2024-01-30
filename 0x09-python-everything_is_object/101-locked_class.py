#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Locked class"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")

    def __getattribute__(self, name):
        if name != "first_name":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")
