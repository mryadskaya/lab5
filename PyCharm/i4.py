#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
# Точность вычислений.
eps = 1e-10
if __name__ == '__main__':
   x = float(input("Value of x? "))
   if x == 0:
       print("Illegal value of x")
       exit(1)
   a = 1
   s, n = a, 0
   # Найти сумму членов ряда.
   while math.fabs(a) > eps:
       a = a * (((-1) * (x ** 2) * (4 * n + 1)) / ((16 * (n ** 3) + 44 * (n ** 2) + 38 * n + 10)))
       s += a
       n += 1
   # Вывести значение функции.
   print(f"C(x) = {s}")


