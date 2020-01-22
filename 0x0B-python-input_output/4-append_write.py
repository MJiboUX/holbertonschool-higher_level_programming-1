#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
       Args:
           filename (str): the file
           text (str): text that will be appended to the file
       Returns: number of characters added
    """
    with open(filename, 'a') as f:
        append_file = f.write(text)
        return(append_file)
