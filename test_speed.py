#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference


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
    # Create table
    wb = Workbook()
    ws = wb.active
    ws.title = "Chart of speed"

    # fill values in cell
    lst = [10, 20, 30, 40, 100, 200, 400, 800, 1000, 1500]
    matrix = [['Кол-во элементов:', 'Время:']]
    for i in range(10):
        result = round(timer(lst[i]), 6)
        matrix.append([lst[i], result])
    for row in matrix:
        ws.append(row)

    # create chart
    chart = LineChart()
    chart.title = "Line Chart"
    chart.style = 13
    chart.x_axis.title = 'Number of values'
    chart.y_axis.title = 'Time'

    data = Reference(ws, min_col=2, min_row=2, max_col=2, max_row=11)
    chart.add_data(data)
    category = Reference(ws, min_row=2, max_row=11, min_col=1, max_col=1)
    chart.set_categories(category)
    ws.add_chart(chart, "A15")

    wb.save('Chart.xlsx')


if __name__ == '__main__':
    create_excel()
