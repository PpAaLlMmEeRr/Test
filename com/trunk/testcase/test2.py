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



    def is_element_available(self, locator):
        if self.driver.is_element_present(locator):
            if self.driver.is_visible(locator):
                return True
            else:
                return False
        else:
            return False
    
    def wait_for_available(self, locator):
        """
        Synchronization to deal with elements that are present, and are visible

        :raises: ElementVisibleTimeout
        """
        for i in range(5):
            try:
                if self.is_element_available(locator):
                    break
            except:
                pass
            time.sleep(1)
        else:
            raise ElementVisibleTimeout("%s availability timed out" % locator)
        return True
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()