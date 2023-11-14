#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    # Вычисляем дискриминант
    D = b ** 2 - 4 * a * c
    if D > 0:
        # Корни квадратного уравнения вещественные
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Корни квадратного уравнения:", x1, x2)
    elif D == 0:
        # Корни квадратного уравнения одинаковые и вещественные
        x = -b / (2 * a)
        print("Уравнение имеет один корень:", x)
    else:
        # Корни квадратного уравнения комплексные
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-D) / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        print("Корни квадратного уравнения:", x1, x2)