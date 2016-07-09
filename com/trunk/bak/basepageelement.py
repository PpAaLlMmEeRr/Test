# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import unittest
import logging
import time
import os
from basepageobject import selenium_server_connection

class BasePageElement(unittest.TestCase):
    pass
    def __get__(self, obj, cls=None):
        selenium_server_connection.get_text(self.locator)

    def __delete__(self, obj):
        pass