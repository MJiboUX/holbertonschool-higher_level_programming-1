#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Inheritance
"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """init class
           Args:
               width (int): width value
               height (int): height value
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle
           Returns: area calculated
        """
        a = self.__width * self.__height
        return(a)

    def __str__(self):
        """Returns: [Rectangle] = <width>/<height>"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
