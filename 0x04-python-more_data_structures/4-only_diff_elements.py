#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set_1.copy() | set_2.copy()
    new = list(set(new))
    for i in set_1:
        for x in set_2:
            if i == x:
                new.remove(x)
    return (new)
