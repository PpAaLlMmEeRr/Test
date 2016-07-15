# -*- coding: utf-8 -*-
'''
Created on 2016年7月15日

@author: palmer
'''
import unittest,time

from com.trunk.bo.loginBO import LoginBO
from com.trunk.page.basepage import BasePage
from com.trunk.page.loginpage import LoginPage
from com.trunk.page.locator import Locator
from com.trunk.actionkeyword import actionKeyword
from com.trunk.seleniumfactory.SeleniumFactory import *

class actTest(unittest.TestCase):

    def setUp(self):
# 开启webdriver
        self.driver = SeleniumFactory().createWebDriver()

    def tearDown(self):
# 关闭webdriver
        self.driver.quit()
        pass


    """脚本的入口引擎"""
    #脚本初始化
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()
        # cls.driver.implicitly_wait(30)
        pathstr = os.path.abspath(os.path.join(os.getcwd(),"..","testdata","logindata.xls"))
        cls.filepath = pathstr

    
    #测试用例
    def action(self, *txt):
        """
        测试Demo
        """
        
        self._page_parameters = {"webdriver":self.driver}
        exeKeyword = actionKeyword.Actionkeywords(**self._page_parameters)
        exeKeyword.setLocatePath(actTest.filepath)
        
        case_id = txt[1]
        username = txt[4]
        password = txt[5]
        # casedata = base.getTabledata(self.filepath, "Test Cases")
        k =4
        stepdata = exeKeyword.getTabledata(self.filepath, "teststep")
        for j in stepdata:
            if txt[0] == j[0]:
                # print j[3]
                if j[3] == "openBrowser":
                    print j[2]
                    exeKeyword.openBrowser()
                elif j[3] == "input_Text":
                    print j[2]
                    loc = exeKeyword.locate(j[4])
                    exeKeyword.input_Text(loc, txt[k])
                    k += 1
                elif j[3] == "click":
                    print j[2]
                    loc = exeKeyword.locate(j[4])
                    exeKeyword.Submit(loc)
                elif j[3] == "verifyLogin":
                    print j[2]
                    loc_1 = exeKeyword.locate(j[4])
                    loc_2 = exeKeyword.locate(j[5])
                    exeKeyword.verifyLogin(loc_1, loc_2)
                elif j[3] == "closeBrowser":
                    print j[2]
                    time.sleep(5)
                    exeKeyword.closeBrowser()
                elif j[3] == "navigate":
                    print j[2]
                    url = j[4]
                    exeKeyword.navigate(url)
                elif j[3] == "clickelement":
                    print j[2]
                    loc = exeKeyword.locate(j[4])
                    exeKeyword.clickElement_i(2, loc)
        pass
    
    @staticmethod
    def getTestFunc(*txt):
        def func(self):
            self.action(*txt)
        return func


    #脚本退出
    @classmethod
    def tearDownClass(cls):
        print "End"
        
def __generateTestCases():
#     login_page = BasePage.Action()
#     driver = SeleniumFactory().createWebDriver()
    print os.getcwd()
    pathstr = os.path.abspath(os.path.join(os.getcwd(),"..","testdata","logindata.xls"))
    casedata = LoginPage.getTabledata(pathstr, "testfunction")
    for i in casedata:
        TCid = i[0]
        if i[3] == "Y":
            print "[Run]"+i[1]+"："
            print " + -"*8
            table = LoginPage.getTabledata(pathstr, "testcases")
            for txt in table:
                if (txt[2] == "Y") & (txt[0] == TCid):
                    print txt
                    setattr(actTest, 'test_%s_%s' % (txt[0], txt[1]), actTest.getTestFunc(*txt))
__generateTestCases()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()