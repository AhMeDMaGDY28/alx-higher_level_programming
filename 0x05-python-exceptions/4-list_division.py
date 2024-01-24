#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for none in range(list_length):
        new.append(0)
    for i in range(0, list_length):
        try:
            new[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
    return new
