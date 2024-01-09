#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Default is empty string.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
