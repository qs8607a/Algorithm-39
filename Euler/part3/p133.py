#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import primes

def f(n):
    """
    >>> f(100)
    454387123
    """
    return sum(p for p in primes(n) if not is_factor_R_10_n(p))


def is_factor_R_10_n(p):
    """测试p是否是R(10**n) {n 为自然数}的因子
    >>> is_factor_R_10_n(3)
    False
    >>> is_factor_R_10_n(11)
    True
    >>> is_factor_R_10_n(17)
    True
    >>> is_factor_R_10_n(43)
    True
    """
    # g(k) = sum(a[k] ** i for i in range(10)) % p
    # a[0] = 10
    # a[n] = 10 ** (10 ** n)
    # a[n + 1] = 10 ** (10 ** (n + 1)) = 10 ** ((10 ** n) * 10) = a[n] ** 10
    a = 10
    while True:
        result = sum(a ** i for i in range(10)) % p
        if result == 0:
            return True
        if a % p == 10 % p:
            return False
        a = a ** 10 % p
    # a[2] = 10 ** 100

