#!/usr/bin/python3

"""Print the sum, difference, multiple and quotient of 10 and 5."""
from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    res_add = add(a, b)
    res_sub = sub(a, b)
    res_mul = mul(a, b)
    res_div = div(a, b)

    print("{} + {} = {}".format(a, b, res_add))
    print("{} - {} = {}".format(a, b, res_sub))
    print("{} * {} = {}".format(a, b, res_mul))
    print("{} / {} = {}".format(a, b, res_div))

if __name__ == "__main__":
    main()
