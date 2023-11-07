#!/usr/bin/python3
"""Defines a function to create an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """Creates a python object from a JSON file."""
    with open(filename) as myFile:
        json.load(myFile)
