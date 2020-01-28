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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id

    def __str__(self):
        """Returns:
               [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """width getter
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle
        """
        return(self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle
           instance with the character #
        """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for l in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """updates the class Rectangle by adding this public method
           that assigns an argument to each attribute
        """
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value
