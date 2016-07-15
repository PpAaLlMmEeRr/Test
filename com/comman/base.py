# -*- coding: utf-8 -*-
'''
Created on 2016年7月15日

@author: Palmer.Piao
'''

class baseObject(object):
    '''
    classdocs
    '''


    def __init__(self,*tupleArg,**dictArg):
        pass
#         for  key in dictArg:
#             if key == "title":
#                 title = dictArg[key]
#                 self.title = title
#                 print self.title
#             elif key == "base_url":
#                 base_url = dictArg[key]
#                 if base_url[-1] != '/': 
#                     base_url += '/'
#                 self.base_url = base_url
#                 print self.base_url
#             elif key == "webdriver":
#                 selenium_driver = dictArg[key]
#                 self.driver = selenium_driver
#                 print self.driver
#         try:
#             self.driver
#         except:
#             print "no driver founed"
    
           
#     def openUrlPage(self, url, title):
#         #使用get打开访问链接地址
#         self.driver.get(url)
#         self.driver.maximize_window()
#         #assert校验，的链接地址是否与配置的地址一致。
#         assert self.checkTitle(title), u"打开开页面失败 . url = %s" % url
#         
#     def checkTitle(self,title):
#         actual_title = self.driver.title
#         return title in actual_title
#     
#     def script(self, src):
#         self.driver.execute_script(src)
