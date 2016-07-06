# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import logging


class BasePage(object):
    '''
    classdocs
    '''
    def __init__(self,selenium_driver,base_url='https://xxxx/'):
        if base_url[-1] != '/': 
            base_url += '/' 
        self.base_url = base_url
        self.driver = selenium_driver
        print "base_url is %s, and driver is %s" % (base_url,selenium_driver)
        #Visit and initialize xpaths for the appropriate page
        self.start() 
        #Initialize the logger object
        
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.debug('This is debug message')
    
    def start(self):
#         self.driver.get(self.base_url)
        assert self.checkTitle("网易"), u"open page failed. url = %s" % self.base_url   
    
    def checkTitle(self,title):
        return "网易"
        pass
    
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
        