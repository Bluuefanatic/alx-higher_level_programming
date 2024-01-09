#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8)

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    
    return num_characters_added
