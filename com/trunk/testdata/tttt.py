# -*- coding: utf-8 -*-
'''
Created on 2016年7月13日

@author: Palmer.Piao
'''

import unittest
from test import test_support
import xlrd



class MyTestCase(unittest.TestCase):
    
    @staticmethod
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
    @staticmethod
    def readxls(filepath, sheetno):
        """
        filepath:文件路径
        sheetno：Sheet编号
        """
        table = MyTestCase.readtable(filepath, sheetno)
        for args in range(1, table.nrows):
            #使用生成器 yield
            yield table.row_values(args)
    
    #读取元素标签和元素唯一标识
    @staticmethod
    def locate(index, filepath="..\\data\\case_data.xls", sheetno=0):
        """
        filepath: 文件路径
        sheetno：Sheet编号
        index: 元素编号
        返回值内容为：("id","inputid")、("xpath","/html/body/header/div[1]/nav")格式
        """
        table = MyTestCase.readtable(filepath, sheetno)
        for i in range(1, table.nrows):
            if index in table.row_values(i):
                return table.row_values(i)[1:3]
      
      
    def setUp(self):
        #some setup code
        pass

    def clear(self):
        #some cleanup code
        pass

    def action(self, arg1, arg2,arg3,arg4):
        print arg1,arg2,arg3,arg4
        pass

    @staticmethod   
    def getTestFunc(arg1, arg2,arg3,arg4):
        def func(self):
            self.action(arg1, arg2,arg3,arg4)
        return func
        
# def __generateTestCases():
#     arglists = [('arg11', 'arg12','arg11', 'arg12'), ('arg21', 'arg22','arg11', 'arg12'), ('arg31', 'arg32','arg11', 'arg12')]
#     for args in arglists:
#         setattr(MyTestCase, 'test_func_%s_%s'%(args[0], args[1]),MyTestCase.getTestFunc(*args) )
# __generateTestCases()
      


def __generateTestCases():
    #test_support.run_unittest(MyTestCase)
    table = MyTestCase.readxls("case_data.xls", 1)
    for txt in table:
#         print txt
        setattr(MyTestCase, 'test_MyTestCase_%s_%s' % (txt[0],txt[1]), MyTestCase.getTestFunc(*txt))
    #     unittest.main()
__generateTestCases()

def test_main():
   
    test_support.run_unittest(MyTestCase)