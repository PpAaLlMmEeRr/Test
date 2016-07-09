# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import unittest
import logging
import time
import os


class BasePageObject(unittest.TestCase):
    pass

class locators():
    pass

class selenium_server_connection():
    connection = ''
    
    def get_text(self,locator):
        return "get text string"
    pass
