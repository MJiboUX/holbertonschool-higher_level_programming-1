#!/usr/bin/python3
"""
Inheritance
"""


def lookup(obj):
    """function that returns the list of available attributes
       and methods of an object.
       Args:
           obj: an object
       Returns:
           a list object
    """
    return(dir(obj))
