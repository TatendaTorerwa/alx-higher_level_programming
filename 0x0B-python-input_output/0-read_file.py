#!/usr/bin/python3
"""Defines a function to read a text file and print to stdout."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
