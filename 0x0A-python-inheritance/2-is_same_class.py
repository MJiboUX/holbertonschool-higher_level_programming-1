#!/usr/bin/python3
"""
Inheritance
"""
def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
       an instance of the specified class ; otherwise False
       Args:
           obj: an object
           a_class: class(type)
       Returns: True or Flase.
    """
    if type(obj) is a_class:
        return(True)
    else:
        return(False)
