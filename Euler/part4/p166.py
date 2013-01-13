#!/usr/bin/env python
#-*- coding:utf-8 -*-

from functools import partial
from operator import add

L = [
        (1, 0,  0,  0,  0,  0,  0,  0),
        (0, 1,  0,  0,  0,  0,  0,  0),
        (0, 0,  1,  0,  0,  0,  0,  0),
        (0, 0,  0,  1,  0,  0,  0,  0),
        (0, 0,  0,  0,  1,  0,  0,  0),
        (0, 0,  0,  0,  0,  1,  0,  0),
        (0, 0,  0,  0,  0,  0,  1,  0),
        (1, 1,  1,  1, -1, -1, -1,  0),
        (0, 0,  0,  0,  0,  0,  0,  1),
        (1, 0,  0, -1,  1,  0, -1,  1),
        (0, 1,  1,  2, -1, -1,  0, -1),
        (0, 0,  0,  0,  0,  1,  1, -1),
        (0, 1,  1,  1, -1,  0,  0, -1),
        (0, 0,  1,  2, -1, -1,  1, -1),
        (1, 0, -1, -1,  1,  1, -1,  1),
        (0, 0,  0, -1,  1,  0,  0,  1),
    ]

def f():
    pass

def g(op, args):
    return reduce(partial(map, op), args)

def check():
    for i in range(4):
        print g(add, [L[i * 4 + j] for j in range(4)])
        print g(add, [L[i + j * 4] for j in range(4)])
    print g(add, [L[0], L[5], L[10], L[15]])
    print g(add, [L[3], L[6], L[9], L[12]])
