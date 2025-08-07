#!/usr/bin/python3
"""
This module defines the Rectangle class
"""


class Rectangle:
    """
    Represents a Rectangle.

    Attributes:
        width (int): The width of a rectangle.
        height (int): The height of a rectangle.

    Methods:
        width: Property getter/setter for width
        height: Property getter/setter for height
        area: Returns the rectangle area.
        perimeter: Returns the rectangle perimeter.
    """

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

    # Getter width
    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width; must be a positive integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height; must be a positive integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "Returns area of Rectangle"
        return self.height * self.width

    def perimeter(self):
        "Returns perimeter of Rectangle"
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using # characters"""
        if self.height == 0 or self.width == 0:
            return ""

        result = []
        for _ in range(self.height):
            result.append("#" * self.width)
        return "\n".join(result)
