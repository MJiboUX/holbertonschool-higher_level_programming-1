"""
Real definition of a rectangle.
Calculates area and parameter.
"""


class Rectangle:
    """A definition of a rectangle.
    Args:
        width (int): width of the Rectangle.
        height (int): height of the Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        else:
            s = (self.width * "#" + "\n") * self.height
            s = s[:-1]
            return(s)

    def __repr__(self):
        return("Rectangle("+str(self.width)+", "+str(self.height)+")")

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((self.width + self.height) * 2)
