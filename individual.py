#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_list(lst, count=0, summ=0):
    if len(lst) == 0:
        return count, summ
    else:
        return sum_of_list(lst[1:], count + 1, summ + lst[0])


if __name__ == "__main__":
    lst = [int(i) for i in input().split()][:-1]
    count, summ = sum_of_list(lst)
    print(f"Количество элементов в списке: {count}")
    print(f"Сумма элементов в списке: {summ}")
