#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(0, list_length):
        div = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            div = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("list_division by 0")
        except IndexError:
            print("out of range")
        finally:
            new.append(div)
    return new
