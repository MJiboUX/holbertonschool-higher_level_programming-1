#!/usr/bin/python3
"""
Reading a file
"""


def read_file(filename=""):
    """function that read a file
       Args:
           filename (str): the file
    """
    with open(filename, 'r') as f:
        read_file = f.read()
        print(read_file, end='')
