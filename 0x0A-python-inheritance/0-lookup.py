#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or attr.startswith("__")]
