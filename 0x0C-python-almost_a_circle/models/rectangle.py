#!/usr/bin/python3
"""
First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
       Attr:
           width(getter/setter)
           height(getter/setter)
           x(getter/setter)
           y(getter/setter)
       Class constructor:
           def __init__(self, width, height, x=0, y=0, id=None)

       Why private attributes with getter/setter? Why not
       directly public attribute?
       Because we want to protect attributes of our class. With a setter
       you are able to validate what a developer is trying to assign to a
       variable. So after, in your class you can trust these attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor, creates a new instance
           of a class
           Args:
               width (int): width of rectangle
               height (int): height of rectangle
               x (int): x-axis
               y (int): y-axis
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id

    @property
    def width(self):
        """width getter
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter
        """
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter
        """
        self.__height = value

    @property
    def x(self):
        """x-axis getter
        """
        return(self.__x)

    @x.setter
    def x(self, value):
        """x-axis setter
        """
        self.__x = value

    @property
    def y(self):
        """y-axis getter
        """
        return(self.__y)

    @y.setter
    def y(self, value):
        """y-axis setter
        """
        self.__y = value
