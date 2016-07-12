# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''

from com.trunk.page.locator import Locator
from com.trunk.page.loginpage import LoginPage
import time

class LoginBO(object):
    locator = Locator()
    
    
    
    def __init__(self,driver):
        self._page_parameters = {"webdriver":driver,"base_url":"http://172.16.15.166/en-us/accounts/login/?next=/zh-cn/","title":"Sign In"}
        self.pageobject = LoginPage(**self._page_parameters)
        
    def run(self):
#         self.locator.getLocator(xpath/css locator,po object) return PO object
#             ._sendKey("admin")
        self.locator.getLocator(LoginPage.getInputField("id=id_usernam1e"),self.pageobject)._sendKey("admin")
        time.sleep(1)
        self.locator.getLocator(LoginPage.getInputField("id=id_password"),self.pageobject)._sendKey("netis")
        time.sleep(1)
        
        
#         self.locator.getLocator(1,2,**self._page_parameters)