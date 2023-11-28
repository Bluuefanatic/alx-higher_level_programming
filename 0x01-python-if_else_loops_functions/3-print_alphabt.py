#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without 'q' and 'e', without a new line
for i in range(97, 123):
    if chr(i) not in ('q', 'e'):
        print("{}".format(chr(i)), end="")
