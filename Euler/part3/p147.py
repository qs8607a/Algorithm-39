#!/usr/bin/env python
#-*- coding:utf-8 -*-
from itertools import product


def f(m, n):
    """
    >>> f(3, 2)
    37
    """
    result = 0
    a =  g(m , n)
    b = 19
    for i, j in product(range(2 * m), range(2 * n)):
        _ = (0, i + j), (2 * m, i + 2 * n - j)
        _ = (2 * m - i, 2 * n + j)
    return a + b

def g(m, n):
    return sum((m - i) * (j + 1) for i in range(m) for j in range(n))
