#!/usr/bin/python3
"""
Inheritance
"""
def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
       or if the object is an instance of a class that inherited from,
       the specified class ; otherwise False
       Args:
           obj: an object
           a_class: class
       Returns: True or False
    """
    if isinstance(obj, a_class) is True:
        return(True)
    else:
        return(False)
