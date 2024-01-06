#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for x in matrix:
            for y in x:
                print("{:d}".format(y), end="")
                if y != x[-1]:
                    print(' ', end="")
            if x != []:
                print("")
    else:
        print("")
