# -*- coding: utf-8 -*-
'''
Created on 2016年7月6日

@author: Palmer.Piao
'''
import unittest


class Test(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
#         selenium_driver,base_url='https://mail.google.com/'
#         if base_url[-1] != '/': 
#             base_url += '/' 
#         self.base_url = base_url
#         self.driver = selenium_driver
#         #Visit and initialize xpaths for the appropriate page
#         self.start() 
#         #Initialize the logger object
#         FILE = os.getcwd()
#         logging.basicConfig(filename=os.path.join(FILE,'log.txt'),level=logging.DEBUG)
#         logging.debug('Debug message2')
        pass

    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(Test("testName")) 
#     unittest.TextTestRunner().run(suite)