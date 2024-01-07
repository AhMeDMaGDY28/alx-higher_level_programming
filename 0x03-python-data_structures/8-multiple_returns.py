#!/usr/bin/python3
def multiple_returns(str):
    a = str[0] if str != "" else None
    length = len(str)
    return length, a
