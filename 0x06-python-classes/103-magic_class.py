#!/usr/bin/python3

"""define MagicClass matching exactly the bytecode provided by Holberton"""

import math

class MagicClass:
    """represent Circle"""

    def __init__(self, radius=0):
        """initialize MagicClass

        Arg:
            radius (float or int): radius of new MagicClass
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return area of MagicClass"""
        return (self__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of MagicClass"""
        return (2 * math.pi * self__radius)
