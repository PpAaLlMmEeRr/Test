# -*- coding: utf-8 -*-
'''
Created on 2016/7/17

@author: palmer
'''
import xlwt,xlsxwriter
from xlrd import open_workbook
from xlutils.copy import copy

if __name__ == '__main__':

    rb = open_workbook('logindata.xls')
    rs = rb.sheet_by_index(0)
    print rb._sheet_names.index("testcases")
    print rb.sheet_by_name("testcases")
    wb = copy(rb)
    ws = wb.get_sheet(2)
#     ws.write(1,10,'changed!')
#     wb.save('logindata.xls')