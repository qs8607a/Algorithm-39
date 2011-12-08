from timeit import Timer
from cProfile import Profile, run
from part3.p129 import main


def test():
    main()
t=Timer("test()","from __main__ import test")
print(t.timeit(1))
run('test()')
