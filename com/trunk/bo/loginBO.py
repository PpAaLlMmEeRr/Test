# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''

from com.trunk.page.locator import Locator
from com.trunk.page.loginpage import LoginPage

class LoginBO(object):
    locator = Locator()
    
    
    def __init__(self,driver):
        self._page_parameters = {"webdriver":driver,"base_url":"http://172.16.15.166/en-us/accounts/login/?next=/zh-cn/","title":"Sign In"}
        
    def run(self):
#         driver.find_element_by_id("id_username").clear()
#         driver.find_element_by_id("id_username").send_keys(result.get("testid"))
        self.locator.getLocator(LoginPage.getInputField("id_username"),LoginPage,**self._page_parameters)._sendKey("testing")
#         self.locator.getLocator(1,2,**self._page_parameters)