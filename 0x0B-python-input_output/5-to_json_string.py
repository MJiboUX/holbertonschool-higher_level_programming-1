#!/usr/bin/python3
"""
To JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
       Args:
           my_obj (object): an object
       Returns: JSON string of my_obj
    """
    json_string = json.dumps(my_obj)
    return(json_string)
