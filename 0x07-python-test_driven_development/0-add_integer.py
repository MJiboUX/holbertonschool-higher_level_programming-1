#!/usr/bin/python3
def add_integer(a, b=98):
    """ Adds two integers

    Args:
        a: first integer
        b: second integer(value of 98 by default)

    Returns:
       integer: The addition of a and b, TypeError otherwise.
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
