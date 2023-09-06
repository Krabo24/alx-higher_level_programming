#!/usr/bin/python3

"""defines Rectangle class"""


class Rectangle:
    """Represent rectangle"""

    def __init__(self, width=0, height=0):
        """initialize new Rectangle

        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width to be integer")
        if value < 0:
            raise ValueError("width to be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height to be integer")
        if value < 0:
            raise ValueError("height to be >= 0")
        self.__height = value

    def area(self):
        """return area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of Rectangle

        Represents rectangle with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
