#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except Exception:
            pass
        except IndexError:
            raise
        else:
            a += 1
    print('')
    return a
