# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
# from com.trunk.other.basepage import BasePage
# from com.trunk.other.loginpage import LoginPage
from selenium.webdriver.remote.webelement import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
class Locator(object):
    wd = None
    page = None
    
    @staticmethod
    def setWd(send_wd):
        wd = send_wd
        print "after setWd, the variable setWd is change to = %s " % wd
    
    def setPage(self,pageObject):
        page = pageObject
    
    
    def getWebELement(self,by):
#         self.wd = webdriver.Chrome()
#         self.wd.find_element(by, value)
#         return self.wd.findElement(by)
        print "getWebEle succ"
        return "getElemenetResult"
    
#     获取元素
    def getLocator(self,by,pageobject):
        element = self.getWebELement(by)
        page = pageobject(self)
        page.setElement(element)
        return page