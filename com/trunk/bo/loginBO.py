# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''

from com.trunk.other.locator import Locator
from com.trunk.other.loginpage import LoginPage

class LoginBO(object):
    locator = Locator()
    
    def run(self):
        self.locator.getLocator(LoginPage.getInputField("linktext"),LoginPage)