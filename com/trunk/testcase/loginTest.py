# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import unittest

from selenium import webdriver

from com.trunk.bo.loginBO import LoginBO
from com.trunk.page.basepage import BasePage
from com.trunk.page.loginpage import LoginPage
from com.trunk.page.locator import Locator


class Test(unittest.TestCase):
    

    def setUp(self):
# 开启webdriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
#         Locator.setDriver(self.driver)
        
        pass
    
        

    def tearDown(self):
#         关闭webdriver
#         self.driver.quit()
#         self.lbo.locator.stoplocator()
        self.driver.quit()
        pass


    def testName(self):
#         测试login
#         wd = "网易"
# #         login_page = LoginPage(wd,"https://172.16.15.166/")
#         lbo = LoginBO()
#         lbo.run()
        self.lbo = LoginBO(self.driver)
        self.lbo.run()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()