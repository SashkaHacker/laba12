import timeit
from functools import lru_cache


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


start_timer = timeit.default_timer()
fib(35)
end_timer = timeit.default_timer()
print(end_timer - start_timer)
