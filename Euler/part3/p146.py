#!/usr/bin/env python
#-*- coding:utf-8 -*-

import operator
from eulertools import is_prime_fast as is_prime

ADD_List = (1, 3, 7, 9, 13, 27)

def f(n):
    """
    x % 21 = 4, 10, 11, 17
    #11914460
    >>> sum(f(15 * (10 ** 7)))
    821107610
    >>> sum(f(2000000))
    1242490
    >>> sum(f(100))
    10
    """
    steps = list(get_steps((3, 7, 13)))
    for k in xrange(0, n, 3 * 7 * 13 * 10):
        for j in steps:
            i = j + k
            if i >= n:
                break
            if i< n and all(map(lambda x:is_prime(i * i + x), ADD_List)):
                yield i


def get_steps(ps):
    r = {}
    for p in ps:
        s = set(map(lambda x: (x *(p - 1))% p, ADD_List))
        r[p] = [i for i in range(p) if (i * 10 * i * 10) % p not in s]

    for i in range(reduce(operator.mul, ps)):
        if all(i %p in r[p] for p in ps):
            yield i * 10

if __name__ == "__main__":
    print list(f(100))
