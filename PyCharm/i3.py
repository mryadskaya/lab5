# !/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, k = map(int, input().split())
    a, b = (10 ** n + k - 1) // k, (10 ** (n + 1) - 1) // k
    print((b - a + 1) * k * (a + b) // 2)
