#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divis = []
    for i in my_list:
        if i % 2 == 0:
            is_divis.append(True)
        else:
            is_divis.append(False)
    return is_divis
