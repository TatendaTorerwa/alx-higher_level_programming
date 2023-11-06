#!/usr/bin/python3
"""Defines a class."""


class BaseGeometry:
    """A public instant method that raises an exception."""
    def area(self):
        raise Exception("area() is not implemented")

    """A public instant method."""
    def integer_validator(self, name, value):
        """It validates a value.

        Args:
            name: The name of the parameter(str).
            value: The paremeter to validate(int).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name_))
