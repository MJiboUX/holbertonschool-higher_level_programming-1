#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """writing into a file
       Args:
           filename (str): the file
           text (str): text that will be written into the file
       Returns: number of characters written
    """
    with open(filename, 'w') as f:
        write_file = f.write(text)
        return(write_file)
