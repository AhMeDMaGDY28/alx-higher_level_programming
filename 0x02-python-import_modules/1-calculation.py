#!/usr/bin/python3
import calculator_1 as mosalah
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {} ".format(a, b, mosalah.add(a, b)))
    print("{} - {} = {}".format(a, b, mosalah.sub(a, b)))
    print("{} * {} = {}".format(a, b, mosalah.mul(a, b)))
    print("{} / {} = {}".format(a, b, mosalah.div(a, b)))

