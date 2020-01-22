#!/usr/bin/python3
"""
From JSON string to Object
"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
       Args:
           my_str (str): string variable
       Returns: an object represented by a JSON string
    """
    json_obj = json.loads(my_str)
    return(json_obj)
