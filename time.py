import timeit
from functools import lru_cache
import sys


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@lru_cache()
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
start_timer = timeit.default_timer()
print(fib(30))
end_timer = timeit.default_timer()
print(end_timer - start_timer)
