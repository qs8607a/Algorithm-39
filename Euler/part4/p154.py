#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import memoized


def f(end = 200000, exp = 12):
    count = 0
    for a in range(end + 1):
        tmp = exp_C(end, a)
        if tmp >= exp:
            count += (end - a + 1)
        else:
            for b in range(end - a + 1):
                if exp_C(end - a, b) + tmp >= exp:
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

from math import factorial

def _f(n, base = 5):
    count = 0
    while n % base == 0:
        n /= base
        count += 1
    return count

def main():
    for i in range(1, 40):
        for line in range(i):
            print " " * (i - line), 
            for n in range(1, line + 2):
                value = factorial(i - 1) / (factorial(line) * factorial(i - 1 - line))
                value *= factorial(line) / (factorial(n - 1) * factorial(line + 1 - n))
                print "{0}".format(_f(value)), 
            print ""
        print "-" * 30

if __name__ == "__main__":
    main()
