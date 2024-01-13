#!/usr/bin/python3
"""
Module containing the Base class.
"""

class Base:
    """
    The Base class for managing the id attribute.
    """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): If provided, assign to the public instance attribute id.
                     Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
