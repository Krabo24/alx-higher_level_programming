#!/usr/bin/python3

"""define class Square"""

class Square:
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new Square

        Args:
            size (int): size of new Square
            position (int, int): position of new square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set current size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get/set current position of Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return current area of Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print Square with the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self__position[0])]
            [print("#", end="") for k in range(0, self__size)]
            print("")

    def __str__(self):
        """define print() representation of Square"""
        if self.__size != 0:
            [print("") for i in range(0, self__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self__position[0])]
            [print("#", end="") for k in range(0, self__size)]
            if i != self.__size - 1:
                print("")
        return ("")
