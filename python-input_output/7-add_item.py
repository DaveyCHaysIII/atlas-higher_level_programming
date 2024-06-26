#!/usr/bin/python3
"""Add command line arguments to list, save"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    arguments = sys.argv[1:]

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    for arg in arguments:
        my_list.append(arg)

    save_to_json_file(my_list, "add_item.json")
