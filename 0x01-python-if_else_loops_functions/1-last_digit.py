#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num2 = abs(number) % 10
if number < 0:
    num2 = -num2
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is 0"
str5 = "and is less than 6 and not 0"
if num2 > 5:
    print(str1, number, str2, num2, str3)
elif num2 == 0:
    print(str1, number, str2, num2, str4)
elif num2 < 6 and num2 != 0:
    print(str1, number, str2, num2, str5)
