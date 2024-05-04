#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lines = dir(hidden_4)
    for i in lines:
        if i[0:2] != '__':
            print(i)
