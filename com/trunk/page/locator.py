# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
from selenium.webdriver.support.wait import WebDriverWait
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

    
#     #重写元素定位方法
#     def find_element(self, *loc):
#         #return self.driver.find_element(*loc)
#         try:
#             WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
#             return self.driver.find_element(*loc)
#         except:
#             print u"%s 页面中未能找到 %s 元素" % (self, loc)
# # 
#     #重写一组元素定位方法
#     def find_elements(self, *loc):
#         #return self.driver.find_element(*loc)
#         try:
#             if len(self.driver.find_elements(*loc)):
#                 return self.driver.find_elements(*loc)
#         except:
#             print u"%s 页面中未能找到 %s 元素" % (self, loc)
            
    def find_element_by_locator(self,pageobject,locator):
        driver = pageobject.getDriverFromPO()
        locator_type = locator[:locator.find("=")]
        if locator_type == "":
            raise InvalidLocatorString(locator)
        locator_value = locator[locator.find("=") + 1:]
        
        if locator_type == 'class':
            by_type = By.CLASS_NAME
#             return WebElement(driver.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            by_type = By.CSS_SELECTOR
#             return WebElement(driver.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            by_type = By.ID
#             return WebElement(driver.find_element_by_id(locator_value))
        elif locator_type == 'link':
            by_type = By.LINK_TEXT
#             return WebElement(driver.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            by_type = By.NAME
#             return WebElement(driver.find_element_by_name(locator_value))
        elif locator_type == 'plink':
            by_type = By.PARTIAL_LINK_TEXT
#             return WebElement(driver.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            by_type = By.TAG_NAME
#             return WebElement(driver.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            by_type = By.XPATH
#             return WebElement(driver.find_element_by_xpath(locator_value))
        else:
            raise InvalidLocatorString(locator)
        try:
            WebDriverWait(driver, 15).until(lambda driver: driver.find_element(by_type,locator_value).is_displayed())
            return driver.find_element(by_type,locator_value)
        except:
#             self不再是driver
            raise ElementNotFound(u"%s 页面中未能找到 %s 元素" % (pageobject.pagename, locator))
        
    def getWebELement(self,pageobject,by):
        return self.find_element_by_locator(pageobject,by)
       
    
#     获取元素
    def getLocator(self,by,pageobject):
        element = self.getWebELement(pageobject,by)
        
        print "element %s" % element
        pageobject.setElement(element)
        return pageobject
    