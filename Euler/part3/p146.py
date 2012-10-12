#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import is_prime_fast as is_prime

def f(n):
    """
    x % 21 = 4, 10, 11, 17
    >>> sum(f(1000000))
    1242490
    >>> sum(f(100))
    10
    """
    for j in xrange((n / 210) + 1):
        tmp = 210 * j
        for i in (tmp + 10, tmp + 80, tmp + 130, tmp + 200):
            if i % 13 not in (1, 3, 4, 9, 10, 12):
                continue
            if i< n and all(map(lambda x:is_prime(i * i + x), (1, 3, 7, 9, 13, 27))):
                yield i
