#!/usr/bin/python3
"""Defines a function that prints a square."""

def print_square(size):
    """Prints a square with a # character.

    Args:
        size: size length of the square.

    Raises:
        TypeError: If the size is ot an integer.
        ValueError: If the size is less than 0.
        TypeError: If the size is a float and is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for m in range(size):
        [print("#", end="") for n in range(size)]
        print("")
