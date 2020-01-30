#!/usr/bin/python3
"""
Base class
"""

import json


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

    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats
           for sharing data representation.
           Returns:
              the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return("[]")
        json_string = json.dumps(list_dictionaries)
        return(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns:
              writes the JSON string representation of list_objs
              to a file
        """
        l = []
        f = cls.__name__ + ".json"
        if list_objs is None:
            return(l)
        with open(f, "w") as f:
            f.write(Base.to_json_string(list_objs))
Base.to_json_string = staticmethod(Base.to_json_string)
