#!/usr/bin/python3
"""
Number of lines
"""


def number_of_lines(filename=""):
    """number of lines of a file
       Args:
           filename (str): the file
       Returns: number of lines
    """
    with open(filename, 'r') as f:
        l = 0
        for i in f:
            l += 1
        return(l)
