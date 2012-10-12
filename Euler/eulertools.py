#-*- coding:utf-8 -*-
import time
from itertools import cycle



def is_square(n):
    """
    >>> is_square(144)
    True
    >>> is_square(12)
    False
    >>> is_square(2 ** 64)
    True
    >>> is_square(2 ** 64 - 1)
    False
    """
    return (int(n ** 0.5) ** 2) == n

def primes(n):
    if n<2:
        raise StopIteration
    else:
        yield 2
        l=[True for i in range((n-1)//2)]
        for i in range(len(l)):
            if l[i]:
                yield 2*i+3
                for j in range(3*i+3,len(l),2*i+3):
                    l[j]=False


def big_primes(begin,end,smallprimes=None):
    '''求begin 到end之间的所有素数，使用smallprimes试除'''
    if smallprimes==None:
        smallprimes=list(primes(int(end**0.5)))
    if 2 in smallprimes:
        smallprimes.remove(2)
    if begin<2:
        begin=3
    if begin==2:
        yield 2
    if begin%2==0:
        begin+=1
    if end%2==0:
        end-=1
    B=[True]*((end-begin+2)//2)
    for p in smallprimes:
        temp=((begin+p-1)//p)*p
        if temp%2==0:
            temp+=p
        if temp==p:
            temp+=2*p
        for j in range((temp-begin)//2,len(B),p):
            B[j]=False
    for i in range(len(B)):
        if B[i]:
            yield 2*i+begin


def exp_mod(a, b, p):
    """(a ** b) % p"""
    if b == 0:
        return 1
    elif b % 2 == 0:
        return ((exp_mod(a, b / 2, p) ** 2) % p)
    else:
        return ((exp_mod(a, b / 2, p) ** 2) * a) % p

def timer(func):
    def wraper(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print time.time() - t
        return result
    return wraper

def convergent_continued_fraction(x):
    a, l = x
    a, b = a, 1
    old_a, old_b = 1, 0
    for n in cycle(l):
        yield a, b
        a, b, old_a, old_b = a * n + old_a, b * n + old_b, a, b


def skip(iter_item, n):
    for i in range(n):
        next(iter_item)
    for item in iter_item:
        yield item
