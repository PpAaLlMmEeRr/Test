# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''

from basepage import BasePage
from selenium.webdriver.remote.webelement import By

class LoginPage(BasePage):
    element = None
    
    def setElement(self, element):
        self.element = element
        print "setElement result is %s" % self.element
    
    @staticmethod
    def getInputField(category):
#         by = By.CSS_SELECTOR("%s" % category)
        return "inputField" 
    
    
    
    def loginMethod(self):
        print "login 的方法"
    
    
    
        