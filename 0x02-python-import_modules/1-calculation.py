#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as mosalah
    a = 10
    b = 5
    print("{} + {} = {} ".format(a, b, mosalah.add(a, b)))
    print("{} - {} = {}".format(a, b, mosalah.sub(a, b)))
    print("{} * {} = {}".format(a, b, mosalah.mul(a, b)))
    print("{} / {} = {}".format(a, b, mosalah.div(a, b)))

