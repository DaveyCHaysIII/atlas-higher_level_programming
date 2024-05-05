#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary_keys = a_dictionary.keys()
    a_dictionary_keys.sort()
    for i in a_dictionary_keys:
        print(i, a_dictionary[i])
