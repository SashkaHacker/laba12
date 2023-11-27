import timeit
from functools import lru_cache
import sys


# @lru_cache
def factorial_recursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


#  @lru_cache
def fib_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursion(n - 2) + fib_recursion(n - 1)


def factorial_iterable(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib_iterable(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == "__main__":
    # sys.setrecursionlimit(5000)
    start_timer = timeit.default_timer()
    fib_recursion(20)
    end_timer = timeit.default_timer()
    print(f'Время выполнения рекурсивной функции: '
          f'{end_timer - start_timer}')
    start_timer = timeit.default_timer()
    fib_iterable(20)
    end_timer = timeit.default_timer()
    print(f'Время выполнения итеративной функции: '
          f'{end_timer - start_timer}')

