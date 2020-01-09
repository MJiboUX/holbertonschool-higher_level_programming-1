#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return(pow(self.size, 2))

    def my_print(self):
        if self.size == 0:
            print()
        if not all(self.position):
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        elif self.position[1] > 0:
            print()
            for i in range(self.size):
                print(" " * self.position[1], end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        elif self.position[1] == 0:
            for i in range(self.size):
                print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
