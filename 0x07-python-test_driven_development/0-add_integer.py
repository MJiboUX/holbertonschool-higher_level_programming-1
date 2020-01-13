#!/usr/bin/python3
""" Addition function
    a: first integer
    b: second integer
    returns: a + b
"""
def add_integer(a, b=98):
    """ Adds two integers
        a, b: integers (can also be floats.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return(a + b)
