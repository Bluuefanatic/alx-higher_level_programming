#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """Add a new attribute if possible, otherwise raise a TypeError."""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
