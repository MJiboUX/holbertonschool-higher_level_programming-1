#!/usr/bin/python3
"""
And now, the Square!
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor, creates a new instance
           of a class
           Args:
               size (int): size of square
               x (int): x-axis
               y (int): y-axis
               id (int): id
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """Returns:
               [Square] (<id>) <x>/<y> - <size>
        """
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width))

    def to_dictionary(self):
        """Returns:
              the dictionary representation of a Square
        """
        d = dict()
        d['id'] = self.id
        d['size'] = self.width
        d['x'] = self.x
        d['y'] = self.y
        return(d)

    @property
    def size(self):
        """size setter
        """
        return(self.width)

    @size.setter
    def size(self, value):
        """size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square
        """
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "size":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
