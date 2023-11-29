#!/usr/bin/python3

def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s  # Return the original string if index is out of bounds

    # Create a copy of the string with the character at position n removed
    return s[:n] + s[n+1:]
