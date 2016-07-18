# -*- coding: utf-8 -*-
'''
Created on 2016/7/17

@author: palmer
'''
import xlwt,xlsxwriter
from xlrd import open_workbook
from xlutils.copy import copy
from com.trunk.actionkeyword.ActionKey import Action

if __name__ == '__main__':

    rb = open_workbook('logindata.xls')
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(2)
    ws.write(1,10,'changed!')
    wb.save('logindata.xls')