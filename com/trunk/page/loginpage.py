# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''

from com.trunk.page.basepage import  BasePage

class LoginPage(BasePage):
    element = None
    
    
    
    @staticmethod
    def getInputField(category):
#         by = By.CSS_SELECTOR("%s" % category)
        return "inputField" 
    
    
    
    def loginMethod(self):
        print "login 的方法"
    
    
    
        