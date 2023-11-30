#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import timeit


def binary_search(element, high, lst, low):
    if high >= low:
        center = (high + low) // 2
        if element > lst[center]:
            return binary_search(element, high, lst, center + 1)
        elif element < lst[center]:
            if center == 0:
                return -1
            return binary_search(element, center, lst, low)
        elif lst[center] == element:
            return center
    else:
        return -1


if __name__ == "__main__":
    # lst = [float(i) for i in input().split()]
    # lst = [randint(0, 1000) for i in range(200)]
    # lst.append(100)
    # lst.sort()
    el = 100

    result = binary_search(el, len(lst) - 1, lst, 0)

    # timer = timeit.timeit(stmt=f'binary_search({el, len(lst) - 1, lst, 0})',
    #                       setup='from __main__ import binary_search',
    #                       globals=globals(),
    #                       number=10)
    # end_timer = timeit.default_timer()
    # print(end_timer - start_timer)
    my_code = '''
    def binary_search(element, high, lst, low):
        if high >= low:
            center = (high + low) // 2
            if element > lst[center]:
                return binary_search(element, high, lst, center + 1)
            elif element < lst[center]:
                if center == 0:
                    return -1
                return binary_search(element, center, lst, low)
            elif lst[center] == element:
                return center
        else:
            return -1
    '''
    # print(timeit.timeit(stmt=my_code))

    if result == -1:
        print('Элемент не найден')
    else:
        print(result)
