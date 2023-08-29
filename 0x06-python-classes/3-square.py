#!/usr/bin/python3

"""define class Square"""

class Square:
    """represent Square"""

    def __init__(self, size=0):
        """initialize new Square

        Args:
            size (int): size of new Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current area of Square."""
        return (self.__size * self.__size)
