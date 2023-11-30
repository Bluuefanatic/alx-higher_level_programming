#!/usr/bin/python3

from sys import argv

def main():
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name

    print("{} argument{}{}:".format(
        num_args,
        's' if num_args != 1 else '',
        '' if num_args == 0 else ':'
    ))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
