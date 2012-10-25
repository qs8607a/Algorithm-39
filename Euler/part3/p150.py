#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import count
from eulertools import memoized

def max_sub_triangle(triangle):
    """
    >>> max_sub_triangle([15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3])
    -42
    """
    for i, v in enumerate(count_triangle_number(), 1):
        if v == len(triangle):
            n = i + 1
            break
        elif v > len(triangle):
            raise Exception()
    result = 0
    for deep, v in enumerate(count_triangle_number(), 1):
        for j in range(deep):
            i = v - deep + j + 1
            for high in range(2, n - deep + 1):
                tmp = sum(sum(triangle[triangle_number(deep + m - 1) + j: triangle_number(deep + m - 1) + j + m + 1]) for m in range(high))
                result = min(result, tmp)
        if deep >= n:
            break

    return result


triangle_number = memoized(lambda x:(x * (x + 1)) / 2)


def count_triangle_number():
    for i in count(1):
        yield triangle_number(i)

