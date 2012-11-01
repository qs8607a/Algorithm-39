#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import memoized


def f(end = 200000, exp = 12):
    count = 0
    for a in range(end + 1):
        tmp = exp_C(end, a)
        for b in range(end - a + 1):
            if exp_C(end - a, b) + tmp > exp:
                count += 1
    return count

@memoized
def count_down(n, base = 5):
    result = 0
    while n > 0:
        n = n / base
        result += n
    return result


def exp_C(a, b):
    return count_down(a) - count_down(b) - count_down(a - b)
