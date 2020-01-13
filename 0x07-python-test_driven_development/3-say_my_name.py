#!/usr/bin/python3
"""
   program that prints "My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Function to print first and last name
       Args:
           first_name: first name
           last_name: last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name is None:
        print("My name is {} ".format(first_name))
    print("My name is {} {}".format(first_name, last_name))
