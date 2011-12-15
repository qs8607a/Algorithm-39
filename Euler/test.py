#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:         llq<llq17501@gmail.com>
"""
from timeit import Timer
from cProfile import run
from part3.p133 import main


def test():
    main()
t=Timer("test()","from __main__ import test")
print(t.timeit(1))
run('test()')
