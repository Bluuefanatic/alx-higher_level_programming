#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
