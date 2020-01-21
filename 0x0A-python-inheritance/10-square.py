#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Inheritance
"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Instantiation with size
           Args:
               size (int): size of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
