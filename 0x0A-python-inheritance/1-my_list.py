#!/usr/bin/python3
"""Defines a subclass MyList."""


class MyList(list):
    """Defines a method to print a sorted list."""
    
    def print_sorted(self):
        """Prints a sorted list."""

        print(sorted(self))
