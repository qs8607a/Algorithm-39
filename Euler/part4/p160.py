#!/usr/bin/env python
#-*- coding:utf-8 -*-


def f(n):
    """
        >>> f(9)
        36288
        >>> f(10)
        36288
        >>> f(20)
        17664
        >>> f(1000000000000)
        1
    """
    re = 1
    for i in range(n):
        re = g(re * g(i + 1))
    return re

def g(v):
    while v % 10 == 0:
        v = v / 10
    return v % 100000

