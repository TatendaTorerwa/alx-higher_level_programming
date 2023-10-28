#!/bin/usr/python3
"""Defines a function to add two integers."""


def add_integer(a, b=98):
	"""Adds two integers or float values.

	Args:
	    a: The first parameter.
	    b: The second parameter.

	Returns:
	    An integer addition of a and b.

	Float values are first typecasted to int before adding them.

	Raises:
	    TypeError: If either a or b is not an integer or a float type.
	"""

	if not isinstance(a, (int, float)):
		raise TypeError("a must be an integer")
	elif not isinstance(b, (int, float)):
		raise TypeError("b must be an integer")
	else:
		return (int(a) + int(b))

