#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary.items()) > 0:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
    else:
        return None
