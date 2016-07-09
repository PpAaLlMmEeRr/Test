# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
# from comcom.trunk.page.basepageport BasePage
# from comcom.trunk.page.loginpageport LoginPage
from selenium.webdriver.remote.webelement import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
class Locator(object):

    _driver = None
    _page = None
    
    @staticmethod
    def setDriver(driver):
        _driver = driver
        print "after setWd, the variable setWd is change to = %s " % _driver
        
    def setPage(self,pageObject):
        _page = pageObject
    
    
    def getWebELement(self,driver,by):
#         self.wd = webdriver.Chrome()
#         self.wd.find_element(by, value)
#         return self.wd.findElement(by)
        print "getWebEle succ"
        print driver
        print by
        print driver.find_element_by_id("id_username")
        return driver.find_element_by_id("id_username")
       
    
#     获取元素
    def getLocator(self,by,pageclass,**dictArg):
        for key in dictArg:
            print "dictArg %s-->%s" %(key,dictArg[key])
            if key == "webdriver":
                self.selenium_driver = dictArg[key]
        
         
        element = self.getWebELement(self.selenium_driver,by)
        print "element %s" % element
        self._page = pageclass(**dictArg)
        self._page.setElement(element)
#         self._page.stopDriver()
        return self._page
#     def getLocator(self,str1,str2,**dictArg):
#         print str1
#         print str2
#         print dictArg
    def _click(self):
        self._page.stopDriver()
        self.click
        
    def stoplocator(self):
        self._page.stopDriver()