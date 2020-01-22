#!/usr/bin/python3
"""
Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
       Args:
           filename (str): the file
    """
    with open(filename, 'r') as f:
        load_json = json.load(f)
        return(load_json)
