#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is lowercase letter and convert to uppercase
        print(
            "{}".format(chr(ord(char) - 32))
            if 97 <= ord(char) <= 122
            else char,
            end=""
        )
    print()  # Print a new line at the end
