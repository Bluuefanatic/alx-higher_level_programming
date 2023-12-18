#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for element in my_list[:x]:
            try:
                print("{:d}".format(element), end=" ")
                printed_integers += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    finally:
        print()
        return printed_integers
