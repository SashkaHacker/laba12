#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from openpyxl import Workbook


def timer(n):
    setup = f'''
from hard import binary_search
from random import randint
lst = [randint(1, 1000) for i in range({n})]
lst.append(100)
lst.sort
el = 100'''
    use = '''
try:
    binary_search(el, len(lst) - 1, lst, 0)
except:
    pass'''

    return timeit.timeit(stmt=use, setup=setup, number=10000)


def create_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Chart of speed"

    # for x in range(1, 101):
    #     for y in range(1, 101):
    #         ws.cell(row=x, column=y)

    ws.cell(row=1, column=1, value="Количество элементов в списке:")
    lst = [10, 20, 30, 40, 100, 200, 400, 800, 1000, 1500]
    matrix = [[] * 10]
    for ind, val in enumerate(lst):
        ws.cell(row=ind + 2, column=1, value=val)

    for i in range(2, 12):
        result = round(timer(lst[i - 2]), 6)
        ws.cell(row=i, column=2, value=result)
    wb.save('Chart.xlsx')


if __name__ == '__main__':
    create_excel()
