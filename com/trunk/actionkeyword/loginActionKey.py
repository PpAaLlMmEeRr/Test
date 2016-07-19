# -*- coding:utf-8 -*-
from docutils.parsers.rst.directives import flag
__author__ = 'tsbc'

from selenium import webdriver
import unittest
import time
import sys
reload(sys)
# from com.trunk.page.basepage import BasePage
from com.trunk.actionkeyword.actionKey import ActionKey
from com.trunk.seleniumfactory.SeleniumFactory import *
from selenium.webdriver.support.wait import WebDriverWait
from xlrd import open_workbook
from xlutils.copy import copy
import xlrd,xlwt

class LoginActionKW(ActionKey):
	"""定义关键字方法"""

	def openBrowser(self):
		"""打开浏览器方法"""
# 		检测浏览器是否打开
		
		self.driver = SeleniumFactory().createWebDriver()
# 		self.driver.implicitly_wait(30)
		pass

	def navigate(self, url):
		"""
		跳转Url地址
		"""
		self.driver.get(url)

	def closeBrowser(self):
		"""关闭浏览器"""
		self.driver.quit()

	#调用send_keys
	def input_Text(self, loc, text):
		"""文本框输入内容"""
		print loc,text
		self.action_send_keys(loc, text)
	#
	def Submit(self, submit_loc):
		"""提交表单"""
		self.find_element(*submit_loc).click()
	
	def clickElement(self, element_loc):
		"""点击按钮"""
		#print self.find_element(*button_loc).text
		self.find_element(*element_loc).click()
	
	def clickButton(self, button_loc):
		"""点击按钮"""
		#print self.find_element(*button_loc).text
		self.find_element(*button_loc).click()

	def clickElement_i(self, index, *element_loc):
		"""点击元素"""
		# print self.find_elements_i(i, *element_loc)
		self.find_elements_i(*element_loc,index=index).click()
	
	def verifyLogin(self, tip_loc, check_login_loc,timeout = 10):
		"""登录校验"""
		
# 		轮询方法，测试跑完一个succ和一个fail的login case，需要平均=62s
# 		-------------------------
		result_dic = {}
		count = 0
		while (count < timeout):
			try:
				WebDriverWait(self.driver, 0.5).until(lambda driver: driver.find_element(*tip_loc).is_displayed())
				ifTipDisplay = True
				print "succ find tip"
				break
			except:
		   		ifTipDisplay = False
		   		print "except from tip_loc check"
		   	try:
				WebDriverWait(self.driver, 0.5).until(lambda driver: driver.find_element(*check_login_loc).is_displayed())
				ifLoginDisplay = True
				print "succ find login"
				break
			except:
		   		print "except from login loc check"
		   		ifLoginDisplay = False
			count = count + 1
			time.sleep(1)
 		
		if ifTipDisplay:
			result_dic['testresult'] = False
			result_dic['msg'] = self.find_element(*tip_loc).text
# 			print self.find_element(*tip_loc).text
			self.saveScreenshot(self.driver, "login_fail")
			return result_dic
		elif ifLoginDisplay:
			print self.driver.title
			result = self.checkTrue(self.driver.find_element(*check_login_loc).text, u"登录失败")
			if result:
				result_dic['testresult'] = True
			else:
				result_dic['testresult'] = False
				result_dic['msg'] = u"登录失败"
			return result_dic
# 			return self.checkTrue(self.driver.find_element(*check_login_loc).text, u"登录失败")
		else:
			result_dic['testresult'] = False
			result_dic['msg'] = "not find both of tip_loc & check_login_loc"
			print "not find both of tip_loc & check_login_loc"
			return result_dic
			
		
# 		-------------------------------------
# 		普通方法，测试跑完一个succ和一个fail的login case，需要平均=73s
# 		spanTF = True
# 		try:
# 			#通过捕获异常，判断是否显示的出了Tip文本，显示为 True 否则为False
# 			self.find_element(*tip_loc).text
# 			spanTF = True
# 		except:
# 			spanTF = False
# 
# 		if spanTF:
# 			print self.find_element(*tip_loc).text
# 		else:
# 			print self.driver.title
# 			self.checkTrue(self.driver.find_element(*check_login_loc).text, u"登录失败")
	
	
	def verifyLogoff(self, username_loc, password_loc,timeout = 10):
		"""登录校验"""
		
# 		轮询方法，测试跑完一个succ和一个fail的login case，需要平均=62s
# 		-------------------------
		result_dic = {}
		count = 0
		while (count < timeout):
			try:
				WebDriverWait(self.driver, 0.5).until(lambda driver: driver.find_element(*username_loc).is_displayed())
				ifUsernameDisplay = True
				print "succ find username_loc"
				break
			except:
		   		ifUsernameDisplay = False
		   		print "except from username_loc check"
		   	try:
				WebDriverWait(self.driver, 0.5).until(lambda driver: driver.find_element(*password_loc).is_displayed())
				ifPasswordDisplay = True
				print "succ find password_loc"
				break
			except:
		   		print "except from password_loc check"
		   		ifPasswordDisplay = False
			count = count + 1
			time.sleep(1)
		
		if ifUsernameDisplay or ifPasswordDisplay:
			result_dic['testresult'] = True
			return result_dic
		else:
			result_dic['testresult'] = False
			result_dic['msg'] = "not find both of username_loc & password_loc"
			print "not find both of username_loc & password_loc"
			self.saveScreenshot(self.driver, "logoff_fail")
			return result_dic	
		
			
	def set_test_result(self,filepath,index,testresult,testcase_name = "testcases", msg_column=9,result_column=10):
		rb = xlrd.open_workbook(filepath, formatting_info=True)
		rs = rb.sheet_by_index(0)
		testcase_name = testcase_name
		sheet_index = rb._sheet_names.index(testcase_name)
		wb = copy(rb)
		ws = wb.get_sheet(sheet_index)
		red   = xlwt.easyxf('font: color-index red, bold on');
		green   = xlwt.easyxf('font: color-index green, bold on');
		if testresult.get('testresult'):
			ws.write(index,result_column,u"pass",green)
		else:
			ws.write(index,msg_column,testresult.get('msg'),red)
			ws.write(index,result_column,u"fail",red)
		wb.save(filepath)


