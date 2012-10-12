#!/usr/bin/env python
#-*- coding:utf-8 -*-
from eulertools import is_square
from collections import defaultdict

def f(n):
    """
    f(120000)

    >>> f(120000)
    32029046
    """
    d = defaultdict(set)
    result = 0
    for r in range(2, n):
        for q in range(1, min(r, n - r)):
            tmp = r + q
            if is_square(tmp * tmp - r * q):
                s = d[q] & d[r]
                if len(s) > 0:
                    for p in s:
                        tmp2 = tmp + p
                        if tmp2 < n:
                            result += tmp2
                d[q].add(r)
                d[r].add(q)
    return result

