#!/usr/bin/python3
"""define class Square"""

class Square:
    """represent Square"""

    def __init__(self, size=0):
        """initialize new Square

        Args:
            size (int): size of new Square
        """
        self.size = size

    @property
    def size(self):
        """get or set current size of Square"""
        return (self.__size)

    @size.setter

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:

            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area of Square"""
        return (self.__size * self.__size)
