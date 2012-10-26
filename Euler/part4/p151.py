#!/usr/bin/env python
#-*- coding:utf-8 -*-

from collections import defaultdict
from fractions import Fraction
from pprint import pprint

def f(n):
    """
    >>> float(f(4))
    0.464398
    """
    statuses = {(0, tuple(1 for i in range(n))) : Fraction(1, 1)}
    for _ in range(2 ** n - 2):
        pprint(dict(statuses))
        new_statuses = defaultdict(Fraction)
        for (day, status), p in statuses.iteritems():
            _sum = sum(status)
            new_day = (day + 1) if _sum == 1 else day
            for i, v in enumerate(status):
                if v != 0:
                    new_statuses[(new_day, cut_in_half(status, i))] += p * Fraction(v, _sum)
        statuses = new_statuses

    return sum(i * v  for (i, _), v in statuses.iteritems())

def cut_in_half(status, use):
    return tuple(v if i < use else v - 1 if i == use else v + 1 for i, v in enumerate(status))


"""
0.46439878160108705
0.464398781601
"""
