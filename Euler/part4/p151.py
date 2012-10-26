#!/usr/bin/env python
#-*- coding:utf-8 -*-

from collections import defaultdict
from fractions import Fraction

def f(n):
    statuses = {tuple(1 for i in range(n)) : Fraction(1, 1)}
    result = 0
    for _ in range(2 ** n - 2):
        new_statuses = defaultdict(Fraction)
        for status, p in statuses.iteritems():
            _sum = sum(status)
            if _sum == 1:
                result += p
                print status, p
            for i, v in enumerate(status):
                if v != 0:
                    new_statuses[cut_in_half(status, i)] += p * Fraction(v, _sum)
        statuses = new_statuses

    return result

def cut_in_half(status, use):
    return tuple(v if i < use else v - 1 if i == use else v + 1 for i, v in enumerate(status))

def g():
    x1 = Fraction(52271, 864000)
    x2 = Fraction(195774400573, 1867017600000)
    x3 = Fraction(7816394518727, 26138246400000)
    x4 = Fraction(7, 36)
    x5 = Fraction(13, 36)
    x6 = Fraction(1, 2)
    p1 = ((x1 - x1 * x4) * ((1 - x2 - x3 + x2 * x6) / (1-x2)) + (x2 - x1 * x4) * ((x2 - x2 * x6) / x2) + (1 - x1 - x2 + x1 * x4) * ((x3 - x2 * x6) / (1-x2)))
    p2 = (x1 * x4 - x1 * x4 * x6 + (x2 - x1 * x4) * x6 + (x1 - x1 * x4) * ((x3 - x2 * x6) / (1-x2)))
    p3 = (x1 * x4 * x6)
    return p1 + p2 * 2 + p3 * 3

print float(g())
