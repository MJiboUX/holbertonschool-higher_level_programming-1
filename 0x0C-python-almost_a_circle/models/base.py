#!/usr/bin/python3
"""
Base class
"""


class Base:
    """Base class:
       This class will be the "base" of all other classes in this project.
       The goal of it is to manage id attribute in all my future classes
       and to avoid duplicating the same code (by extension, same bugs)
       Attr:
           nb_objects (private): number of objects
       Class constructor:
           def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor, creates a new instance
           of a class
           Args:
               id (int): id of base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
