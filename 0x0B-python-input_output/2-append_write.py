#!/usr/bin/python3
"""Defines a function that appends a string to end of text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of UTF8 file.
    Args:
        filename: The file to append text to.
        text: The text to append to file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
