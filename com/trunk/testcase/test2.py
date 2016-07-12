# -*- coding: utf-8 -*-
'''
Created on 2016年7月12日

@author: palmer
'''

from com.trunk.bo.loginBO import LoginBO
from com.trunk.page.basepage import BasePage
from com.trunk.page.loginpage import LoginPage
from com.trunk.page.locator import Locator
from com.trunk.seleniumfactory.SeleniumFactory import *
from com.trunk.exception.Exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest,time


class Test(unittest.TestCase):

    def setUp(self):
# 开启webdriver
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)
#         self.driver = SeleniumFactory().createWebDriver()
        
        self.driver = SeleniumFactory().create()

    def tearDown(self):
#         关闭webdriver
#         self.driver.quit()
        pass
    
    def testName(self):
        base_url = "http://172.16.15.166/en-us/accounts/login/?next=/zh-cn/"
#         self.driver.
#         self.driver.get(base_url)
        self.driver.open(base_url)
        self.is_element_available("css=#id_password")


#     #重写元素定位方法
#     def find_element(self, *loc):
#         #return self.driver.find_element(*loc)
#         try:
#             WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
# #             WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, csslocator)))
# #             WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,csslocator)))
#             return self.driver.find_element(*loc)
#         except:
#             print u"%s 页面中未能找到 %s 元素" % (self, loc)
# 
#     #重写一组元素定位方法
#     def find_elements(self, *loc):
#         #return self.driver.find_element(*loc)
#         try:
#             if len(self.driver.find_elements(*loc)):
#                 return self.driver.find_elements(*loc)
#         except:
#             print u"%s 页面中未能找到 %s 元素" % (self, loc)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()