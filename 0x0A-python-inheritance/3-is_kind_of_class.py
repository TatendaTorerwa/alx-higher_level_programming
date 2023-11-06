#!/usr/bin/python3
"""Defines a class and inherited class checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to be checked.
        a_class: The type of class to be checked.
    Returns:
        True - If an object is an instance of a class or inherited class
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
