#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import factorial


def f():
    return max(p(n) for n in range(2, 26 + 1))


def p(n):
    for i in range(n - 1):
        i, n - 1 - i
        for x in range(26):
            pass


def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
