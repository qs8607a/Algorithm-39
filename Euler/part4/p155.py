#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fractions import Fraction
from collections import defaultdict
from itertools import product

STANDARD = Fraction(60, 1)

def D(n):
    """
    #298.85s  == 6 min
    >>> D(18)
    3857447
    >>> D(1)
    1
    >>> D(2)
    3
    >>> D(3)
    7
    """
    M = defaultdict(set)
    M[1].add(STANDARD)
    for use_unit in range(2, n + 1):
        for i in range(1, n / 2 + 1):
            j = use_unit - i
            for a, b in product(M[i], M[j]):
                x, y = a + b, (a * b) / (a + b)
                M[use_unit].update((x, y))
    return len(reduce(lambda x,y:x.union(y), M.values()))

