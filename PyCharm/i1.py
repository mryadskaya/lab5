#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    m = int(input("Введите номер месяца:"))
    if m == 2:
        print("В феврале 28 или 29 дней")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("В этом месяце 30 дней")
    else:
        print("В этом месяце 31 день")