#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = roman_dic.get(char, 0)
        if prev_value > value:
            sum -= value
        else:
            sum += value
        prev_value = value
    return sum
