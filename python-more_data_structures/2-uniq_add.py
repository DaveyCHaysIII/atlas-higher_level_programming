#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = []
    for i in my_list:
        if i not in uniques:
            uniques.append(i)
    sum = 0
    for x in uniques:
        sum += x
    return sum
