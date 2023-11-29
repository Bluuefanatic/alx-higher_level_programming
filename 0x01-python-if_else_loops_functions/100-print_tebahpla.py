#!/usr/bin/python3

# Print the ASCII alphabet in reverse order, alternating lowercase, uppercase
for i in range(122, 96, -1):
    case = chr(i).lower() if (122 - i) % 2 == 0 else chr(i).upper()
    print("{}".format(case), end="")
