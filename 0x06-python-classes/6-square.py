#!/usr/bin/python3

"""define class Square."""


class Square:
    """represent Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize new Square

        Args:
            size (int): size of new Square
            position (int, int): position of new Square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """get or set current size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a integer")
        elif value < 0:
            raise ValueError("size should be >= 0")
        self.__size = value

    @property
    def position(self):
        """get or set current position of Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return current area of Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print Square with the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
