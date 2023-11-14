#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
PI = 3.1415926535
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Value of x?"))
    if x == 0:
        print("Illegal value of x?")
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        a = ((-1) ** n *(PI/2) ** (2 * n)) / (math.factorial(2 * n) * (4 * n + 1))
    print(f"C(x) = {S}")


