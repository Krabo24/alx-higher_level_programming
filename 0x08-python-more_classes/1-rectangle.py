#!/usr/bin/python3

"""Defines a Rectangle class"""

class Rectangle:
    """represent rectangle"""

    def __init__(self, width=0, height=0):
        """initialize new Rectangle

        Args:
            width (int): width of new rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width to be integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value
