#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import count
from bisect import insort_left

def f(n):
    """
    >>> f(1)
    2
    >>> f(2)
    15
    >>> f(3)
    104
    >>> f(4)
    714
    >>> f(10)
    p74049690
    """
    index = 0
    for a, b, c in Pythagorean_triple_genertor():
        if 2 * (a - 1) == b:
            index += 1
            if index == n:
                return a - 1


def Pythagorean_triple_genertor():
    ls = []
    m = 2
    a, b, c = 0, 0, 0
    while True:
        if 2 * m - 1 < a or len(ls) == 0:
            for n in range(1, m):
                a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
                if b < a:
                    a,b = b,a
                insort_left(ls, (a, b, c))
            m += 1
        a, b, c = ls.pop(0)
        if 2 * m - 1 < a:
            ls.insert(0, (a, b, c))
        else:
            yield a, b, c
