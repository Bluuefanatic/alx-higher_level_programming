#!/usr/bin/python3

# Print the ASCII alphabet in reverse order, alternating lowercase and uppercase
for i in range(122, 96, -1):
    print("{}".format(chr(i)), end="")
