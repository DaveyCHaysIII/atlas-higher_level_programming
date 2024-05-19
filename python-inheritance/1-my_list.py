#!/usr/bin/python3
"""Print a sorted list"""


class MyList(list):
    """
    All lists should hold integer values
    """

    def print_sorted(self):
        """prints integer values in ascending order"""

        print(sorted(self))
