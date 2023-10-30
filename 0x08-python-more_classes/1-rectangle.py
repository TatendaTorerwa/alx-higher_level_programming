#!/usr/bin/python
"""Defines a rectangle class."""


class Rectangle:
    """A rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Get the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Set a value to the width."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Retrieve the height otf the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Set a value to the height."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
