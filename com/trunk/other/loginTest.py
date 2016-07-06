# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import unittest

from com.trunk.other.loginpage import LoginPage
from com.trunk.bo.loginBO import LoginBO
class Test(unittest.TestCase):


    def setUp(self):
# 开启webdriver
        pass


    def tearDown(self):
#         关闭webdriver
        pass


    def testName(self):
#         测试login
        wd = "网易"
#         login_page = LoginPage(wd,"https://172.16.15.166/")
        lbo = LoginBO()
        lbo.run()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()