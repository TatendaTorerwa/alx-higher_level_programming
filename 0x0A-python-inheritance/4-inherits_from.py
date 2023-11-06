#!/usr/bin/python3
"""Defines an inherited class checking function."""


def inherits_from(obj, a_class):
    """Checks ifan object is a subclass.

    Args:
        obj: The object to be checked.
        a_class: The type of class.

    Returns:
        True - If the object is a subclass
        Otherwise - False.
    """

     return isinstance(obj, a_class) and type(obj) != a_class
