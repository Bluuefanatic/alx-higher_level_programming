#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """Custom list class with additional method."""

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
