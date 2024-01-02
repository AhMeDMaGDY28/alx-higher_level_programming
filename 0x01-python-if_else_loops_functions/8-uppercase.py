#!/usr/bin/python3

def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    print("{}".format(result))
