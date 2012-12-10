#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fractions import Fraction

def f(val, min_, max_):
    """
        #>>> f(Fraction(1, 2), 2, 80)
        ?
        >>> f(Fraction(1, 2), 2, 45)
        3
    """
    A = []
    tmp = 0
    for v in reversed(range(min_, max_ + 1)):
        tmp += Fraction(1, v * v)
        A.insert(0, tmp)

    if val + val > A[0]:
        val = A[0] - val

    queue = [(val, min_)]
    index = 0
    counter = 0
    print "Begin :"
    while index < len(queue):
        val, now = queue[index]
        print index, now
        remain = A[now - 2] #TODO check
        if val == remain or val == 0:
            counter += 1
        elif 0 < val < remain:
            queue.append((val, now + 1))
            queue.append((val - Fraction(1, now * now), now + 1))

        index += 1

    return counter


def main():
    print f(Fraction(1, 2), 2, 45)

if __name__ == "__main__":
    main()
