#!/usr/bin/python3
"""Defines a function to write string to a text file and return characters written."""


def write_file(filename="", text=""):
    """Return number of chararcters written to UTF8.
    Args:
        filename: The file to be written to or created.
        text: The text to be written to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
