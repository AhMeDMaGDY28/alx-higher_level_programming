#!/usr/bin/python3
def magic_string():
    global a, a = 1 if 'a' not in globals() else a + 1
    return "BestSchool" * a if a == 1 else "BestSchool, " * a
