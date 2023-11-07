#!/usr/bin/python3
"""Defines student class."""


class Student:
    """Represent a student class."""
    def __init__(self, first_name, last_name, age):
        """A class constructor.
        Args:
            first_name(str): The first name of the student.
            last_name(str): The second name of the student.
            age(int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Retrieves a dictionary representation of a Student."""
            return self.__dict__
