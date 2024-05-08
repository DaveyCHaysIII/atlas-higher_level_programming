#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val_printed = True
        print("{:d}".format())
    except TypeError:
        val_printed = False
    finally:
        return val_printed
