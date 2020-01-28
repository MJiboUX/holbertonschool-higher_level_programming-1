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
