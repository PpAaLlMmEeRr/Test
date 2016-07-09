# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import logging
from selenium import webdriver

class BasePage(object):
    '''
    classdocs
    '''
    def __init__(self,*tupleArg,**dictArg):
        for  key in dictArg:
            if key == "title":
                title = dictArg[key]
                self.title = title
                print self.title
            elif key == "base_url":
                base_url = dictArg[key]
                if base_url[-1] != '/': 
                    base_url += '/'
                self.base_url = base_url
                print self.base_url
            elif key == "webdriver":
                selenium_driver = dictArg[key]
                self.driver = selenium_driver
                print self.driver
        
        try:
            self.driver
        except:
            print "no driver founed"
#             self.driver = webdriver.Chrome()



#         try:
#             print "base_url is %s, and driver is %s" % (base_url,selenium_driver)
#         except:
#             print "base_url is %s" % (base_url)
        #Visit and initialize xpaths for the appropriate page
        self.start() 
        #Initialize the logger object
        
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.debug('This is debug message')
#         self.stopDriver()
    
    def start(self):
        self.driver.get(self.base_url)
        assert self.checkTitle(self.title), u"open page failed. url = %s" % self.base_url  
    
#     @staticmethod
    def stopDriver(self):
        self.driver.quit()
    
    def checkTitle(self,title):
#         _re = title in self.driver.title
        print "driver.title = %s" % self.driver.title
        print "title %s" % title
        return title in self.driver.title
    
    def openUrl(self):
        pass
    
    def sendText(self):
        pass
    
    def click(self):
        pass

#     def findElement(self):
#         wd.find_element(by, value)
#         pass
    
    def findElements(self):
        pass    
    
    
    def setElement(self, element):
        self.element = element
        print "setElement result is %s" % self.element
        
    def _sendKey(self, value):
        self.element.send_keys(value)
        print "setElement result is %s" % self.element
        