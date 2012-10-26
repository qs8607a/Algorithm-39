#!/usr/bin/env python
#-*- coding:utf-8 -*-
from itertools import product


def f(m, n):
    """
    >>> f(47, 43)
    1
    >>> f(1, 1)
    1
    >>> f(2, 1)
    4
    >>> f(3, 1)
    8
    >>> f(2, 2)
    18
    >>> f(3, 2)
    37
    """
    result = 0
    for a, b in product(range(1, max(m, n) +1), range(1, max(n, m) + 1)):
        tmp = 0
        for i in range(a, 2 * n - b + 1):
            if i % 2 == 1:
                t = (2 * m + 1 - (a + b )) / 2
            else:
                t = m - (a + b - 1) / 2
            tmp += t
        result += tmp
    result += g(m, n)
    return result

def g(m, n):
    return sum((m - i) * (j + 1) for i in range(m) for j in range(n))
