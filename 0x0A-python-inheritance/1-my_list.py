#!/usr/bin/python3
"""
Inheritance
"""


class MyList(list):
    """MyList class that inherits from list
    """
    def print_sorted(self):
        """function that prints the list sorted
        """
        return(print(sorted(self)))
