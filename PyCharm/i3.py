#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    n = int(input("Введите значение n: "))
    k = int(input("Введите значение k: "))
    total_sum = 0
    for i in range(10 ** (n - 1), 10 ** n):
        if i % k == 0:
            total_sum += i
    print("Сумма всех", n, "-значных чисел, кратных", k, ":", total_sum)