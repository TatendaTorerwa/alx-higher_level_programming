#!/usr/bin/python3
"""Defines a class."""


class BaseGeometry:
    """Public instant method that raises an exception."""

    def area(self):
        """Exception raised."""
        raise Exception("area() is not implemented")
