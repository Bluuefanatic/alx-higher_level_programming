#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to text file (UTF-8), returns the number written.

    Args:
        filename (str): The name of the file to write. Default is empty string
        text (str): The string to write to the file. Default is an empty string

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters = file.write(text)
    
    return num_characters

# Example usage
if __name__ == "__main__":
    filename = "example.txt"  # Replace with your desired file name
    text_to_write = "Hello, this is a sample text to be written to the file."
    
    num_chars_written = write_file(filename, text_to_write)
    print(f"{num_chars_written} characters written to {filename}")
