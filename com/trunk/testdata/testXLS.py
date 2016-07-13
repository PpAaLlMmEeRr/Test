# -*- coding: utf-8 -*-
'''
Created on 2016年7月13日

@author: Palmer.Piao
'''
#读取excel文件的table
from argparse import Action

import xlrd


# @staticmethod
def readtable(filepath, sheetno):
    """
    filepath:文件路径
    sheetno：Sheet编号
    """
    data = xlrd.open_workbook(filepath)
    #通过索引顺序获取Excel表
    table = data.sheets()[sheetno]
    return table

#读取xls表格，使用生成器yield进行按行存储
# @staticmethod
def readxls(filepath, sheetno):
    """
    filepath:文件路径
    sheetno：Sheet编号
    """
    table = readtable(filepath, sheetno)
    for args in range(1, table.nrows):
        #使用生成器 yield
        yield table.row_values(args)

#读取元素标签和元素唯一标识
# @staticmethod
def locate(index, filepath="..\\data\\case_data.xls", sheetno=0):
    """
    filepath: 文件路径
    sheetno：Sheet编号
    index: 元素编号
    返回值内容为：("id","inputid")、("xpath","/html/body/header/div[1]/nav")格式
    """
    table = readtable(filepath, sheetno)
    for i in range(1, table.nrows):
        if index in table.row_values(i):
            return table.row_values(i)[1:3]
    
if __name__ == '__main__':
    table = readxls("logindata.xls", 1)
    for txt in table:
        print txt
#     setattr(Caselogin126mail, 'test_login126mail_%s_%s' % (txt[0],txt[1]), Caselogin126mail.getTestFunc(*txt))
    pass