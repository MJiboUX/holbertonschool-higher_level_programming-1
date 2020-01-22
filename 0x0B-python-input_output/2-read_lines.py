#!/usr/bin/python3
"""
Read lines
"""


def read_lines(filename="", nb_lines=0):
    """reads lines from a file
       Args:
           filename (str): the file
           nb_lines (int): number of lines that will be read
       Returns: the lines that will be read
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            read_file = f.read()
            print(read_file, end='')
        else:
            for i in range(nb_lines):
                read_file = f.readline()
                print(read_file, end='')
