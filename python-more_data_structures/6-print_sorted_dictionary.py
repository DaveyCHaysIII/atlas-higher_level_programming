#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    keys.sort()
    for i in keys:
        print(i, a_dictionary[i])
