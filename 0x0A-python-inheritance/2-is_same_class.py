#!/usr/bin/python3
"""Defines a function to check the instance of objecct."""


def is_same_class(obj, a_class):
    """Checks the instance.

    Args:
        obj: The object to be checked.
        a_class: The class to match the type of obj to.
    Returns:
        True - if obj is an instance of clas a_class
        Otherwise - False.
    """

    if type(obj) == a_class:
        return True
    return False
