#!/usr/bn/python3
"""Defines a subclass."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An inherited class from BaseGeometry."""

    def __init__(self, width, height):
        """A constructor function

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
