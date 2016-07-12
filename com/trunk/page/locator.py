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
from com.trunk.exception.Exceptions import *
from selenium.selenium import selenium
class Locator(object):

#     _driver = None
#     _page = None
#     
#     @staticmethod
#     def setDriver(driver):
#         _driver = driver
#         print "after setWd, the variable setWd is change to = %s " % _driver
#         
#     def setPage(self,pageObject):
#         _page = pageObject
    def find_element_by_locator(self,driver, locator):
        locator_type = locator[:locator.find("=")]
        if locator_type == "":
            raise InvalidLocatorString(locator)
        locator_value = locator[locator.find("=") + 1:]
        if locator_type == 'class':
            return WebElement(driver.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(driver.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            return WebElement(driver.find_element_by_id(locator_value))
        elif locator_type == 'link':
            return WebElement(driver.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            return WebElement(driver.find_element_by_name(locator_value))
        elif locator_type == 'plink':
            return WebElement(driver.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            return WebElement(driver.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            return WebElement(driver.find_element_by_xpath(locator_value))
        else:
            raise InvalidLocatorString(locator)
    
    def getWebELement(self,pageobject,by):
#         self.wd = webdriver.Chrome()
#         self.wd.find_element(by, value)
#         return self.wd.findElement(by)
#         print "getWebEle succ"
#         print driver
#         print by
#         print driver.find_element_by_id(by)
        
        pageobject.wait_for_available("css=#id_password")
        
        driver = pageobject.getDriverFromPO()
#         selenium.is_element_present(By.ID,"id_password")
        
#         return driver.find_element_by_id(by)
        return self.find_element_by_locator(driver,by)
       
    
#     获取元素
    def getLocator(self,by,pageobject):
#         for key in dictArg:
#             print "dictArg %s-->%s" %(key,dictArg[key])
#             if key == "webdriver":
#                 self.selenium_driver = dictArg[key]
        
#         self._page = pageclass(**dictArg)
        self.selenium_driver = pageobject.getDriverFromPO()
        
        element = self.getWebELement(pageobject,by)
        
        print "element %s" % element
        pageobject.setElement(element)
        return pageobject
    