# -*- coding: utf-8 -*-
'''
Created on 2016年7月15日

@author: palmer
'''
import unittest,time,os
# import xlrd,xlsxwriter
from com.trunk.actionkeyword import loginActionKey
# from com.trunk.actionkeyword.actionKey import ActionKey
from com.trunk.actionkeyword.loginActionKey import LoginActionKW

class actTest(unittest.TestCase):

    def setUp(self):
# 开启webdriver
#         self.driver = SeleniumFactory().createWebDriver()
        pass

    def tearDown(self):
# 关闭webdriver
#         self.driver.quit()
        pass


    """脚本的入口引擎"""
    #脚本初始化
    @classmethod
    def setUpClass(cls):
        cls.dur_time_start = time.time()
        pathstr = os.path.abspath(os.path.join(os.getcwd(),"..","testdata","logindata.xls"))
        cls.filepath = pathstr
    
    #脚本退出
    @classmethod
    def tearDownClass(cls):
        cls.dur_time_stop = time.time()
        print cls.dur_time_stop - cls.dur_time_start
        print "End"
    
    #测试用例
    def action(self, sheetname,index, *txt):
        """
        测试Demo
        """
        try:
            exeKeyword = loginActionKey.LoginActionKW()
            exeKeyword.setLocatePath(actTest.filepath)
            
            case_id = txt[1]
            username = txt[4]
            password = txt[5]
    #         testresult = txt[10]
            k =4
            stepdata = exeKeyword.getTabledata(self.filepath, sheetname)
            
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
                    elif j[3] == "verifyLoginWithSetResult":
                        print j[2]
                        loc_1 = exeKeyword.locate(j[4])
                        loc_2 = exeKeyword.locate(j[5])
                        testresult = exeKeyword.verifyLogin(loc_1, loc_2)
                    
                    elif j[3] == "verifyLogoffWithSetResult":
                        print j[2]
                        loc_1 = exeKeyword.locate(j[4])
                        loc_2 = exeKeyword.locate(j[5])
                        testresult = exeKeyword.verifyLogoff(loc_1, loc_2)
                    
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
    #                     exeKeyword.clickElement_i(1, loc)
                        exeKeyword.clickElement(loc)
            
            
            exeKeyword.set_test_result(actTest.filepath, index, testresult)
        except Exception as e:
#             result_dic = {}
#             result_dic['testresult'] = "Block"
#             result_dic['msg'] = e.ToString()
            testresult = {"testresult":"Block","msg":"e"}
            exeKeyword.set_test_result(actTest.filepath, index, testresult)
    
    @staticmethod
    def getTestFunc(index,*txt):
        def func(self):
            self.action(index,*txt)
        return func


    
        
def __generateTestCases():
    print os.getcwd()
    pathstr = os.path.abspath(os.path.join(os.getcwd(),"..","testdata","logindata.xls"))
    print pathstr
    casedata = LoginActionKW.getTabledata(pathstr, "testfunction")
    for i in casedata:
        TCid = i[0]
        if i[3] == "Y":
            print "[Run]"+i[1]+"："
            print " + -"*8
            
            sheetname = i[2]
            if not LoginActionKW.checkSheetName(pathstr, sheetname):
                sheetname = "teststeps"
                
            table = LoginActionKW.getTabledata(pathstr, "testcases")
            for index,txt in enumerate(table):
                if (txt[2] == "Y") & (txt[0] == TCid):
                    print txt
                    row_num = index+1
                    setattr(actTest, 'test_%s_%s' % (txt[0], txt[1]), actTest.getTestFunc(sheetname,row_num,*txt))
__generateTestCases()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()