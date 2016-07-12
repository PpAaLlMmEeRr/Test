# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import time,unittest

from selenium import webdriver

from com.trunk.bo.loginBO import LoginBO
from com.trunk.page.basepage import BasePage
from com.trunk.page.loginpage import LoginPage
from com.trunk.page.locator import Locator
from com.trunk.seleniumfactory.SeleniumFactory import *

class Test(unittest.TestCase):
    

    def setUp(self):
# 开启webdriver
        self.driver = SeleniumFactory().createWebDriver()

    def tearDown(self):
#         关闭webdriver
        self.driver.quit()
        pass


    def testLoginSuccess(self):
#         测试login
        self.lbo = LoginBO(self.driver)
        self.lbo.run()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()