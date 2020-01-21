#!/usr/bin/python3
"""
Inheritance
"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance
       of a class that inherited (directly or indirectly) from
       the specified class ; otherwise False
       Args:
           obj: an object
           a_class: class
       Returns: True or False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return(True)
    else:
        return(False)
