#!/usr/bin/env python
#-*- coding:utf-8 -*-

from collections import defaultdict
from fractions import Fraction

def f():
    statuses = {(1, 1, 1, 1) : Fraction(1, 1)}
    result = 0
    for _ in range(14):
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

def mul(a, b):
    return a[0] * b[0], a[1] * b[1]

def add(a, b):
    return (a[0] * b[1] + a[1] * b[0]) , a[1] * b[1]

def cut_in_half(status, use):
    return tuple(v if i < use else v - 1 if i == use else v + 1 for i, v in enumerate(status))

print float(f())
