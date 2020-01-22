#!/usr/bin/python3
"""
Student to JSON with filter
"""


class Student:
    """Student class
       Public attributes:
            first_name
            last_name
            age
    """
    def __init__(self, first_name, last_name, age):
        """init instance
           Args:
               first_name (str): first name of student
               last_name (str): last name of student
               age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
           Args:
               attrs: attributes
           Returns: dictionary of attribute names contained in the list,
                    else all attributes must be retrieved if it's a list
                    of strings
        """
        if type(attrs) is list:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return(my_dict)
        return(self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
           Args:
               json (dict): json dictionary
        """
        self.__dict__ = dict(json)
        return(self.__dict__)
