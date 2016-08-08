# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import time, unittest

from selenium import webdriver

from com.trunk.bo.loginBO import LoginBO
from com.trunk.page.basepage import BasePage
from com.trunk.page.locator import Locator
from com.trunk.page.loginpage import LoginPage
from com.trunk.seleniumfactory.SeleniumFactory import *
import unit_create_spv, unit_create_sp


class Test(unittest.TestCase):
    

    def setUp(self):
# 开启webdriver
        os.environ["SELENIUM_DRIVER"]="sauce-ondemand:?browser=googlechrome"
        os.environ["SELENIUM_HOST"]="172.16.103.222"
        os.environ["SELENIUM_PORT"]="4444"
        os.environ["SELENIUM_STARTING_URL"]="http://www.baidu.com"
#         self.driver = SeleniumFactory().createWebDriver()
        self.driver = webdriver.Chrome()
        
        pass

    def tearDown(self):
#         关闭webdriver
        self.driver.quit()
        pass


    def testLoginSuccess(self):
       
#         for k,v in os.environ.iteritems():
#             print k,v
#         print os.environ["palmer"]
#         self.driver.get("http://www.baidu.com")

#         测试login
#         unit_create_spv.runit(self.driver)
        print self.driver._is_remote
        
#         unit_create_sp.runit(self.driver)

#         self.lbo = LoginBO(self.driver)
# # #         self.lbo.start()
#         self.lbo.run()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()