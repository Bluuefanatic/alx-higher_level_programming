#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    res_add = add(a, b)
    res_sub = sub(a, b)
    res_mul = mul(a, b)
    res_div = div(a, b)

    print(res_add)
    print(res_sub)
    print(res_mul)
    print(res_div)
