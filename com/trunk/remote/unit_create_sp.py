# -*- coding: utf-8 -*-
'''
Created on 2015年12月22日

@author: Palmer.Piao
'''
import unittest,time,csv,os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    pass

def login(driver,result):
    # ERROR: Caught exception [ERROR: Unsupported command [getEval | new Array("172.16.15.167") | ]]
    # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['smartprobe_ip'].length | ]]
    driver.find_element_by_id("id_username").clear()
    driver.find_element_by_id("id_username").send_keys(result.get("testid"))
    driver.find_element_by_id("id_password").clear()
    driver.find_element_by_id("id_password").send_keys(result.get("testpwd"))
    driver.find_element_by_css_selector("button.btn.btn-primary").click()
    pass
    
def parseCsv(csvpath):
    csvpath = csvpath
    csvfile=open(csvpath, 'rb')
    reader = csv.reader(csvfile)
    result={}
    for row in reader:
#             result[row[0]]=row[1:]#value存成list
        result[row[0]]=row[1]#value存成string
    csvfile.close()
    return result

def runit(driver):
#     driver=webdriver.Chrome()

    


    try:
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        print dirname, filename
    except Exception as Err:
        dirname = os.getcwd()
        pass
#     csvpath = dirname+"/../../../sources/BCO.csv"
#     csvpath = os.path.abspath(os.path.join(dirname,"..","..","..","sources","BCO.csv"))
    csvpath = os.path.abspath(os.path.join(dirname,"..","testdata","BCO.csv"))
    result=parseCsv(csvpath)
    base_url=result.get("base_url")
    smart_ip = result.get("smart_ip")
    smart_name = result.get("smart_name")
    url = base_url+"/zh-cn/accounts/login/?next=/zh-cn/manager/sp/server/"
    print url
    driver.get(url)
    login(driver,result)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.discovery-list.xtable-container.dark")))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.create")))
    driver.find_element_by_css_selector("button.btn.btn-primary.create").click()
    driver.find_element_by_css_selector("td.value > input[type='text']").clear()
    driver.find_element_by_css_selector("td.value > input[type='text']").send_keys(smart_ip)
    driver.find_element_by_xpath(u"//label[text()=\"Smart Probe 别名\"]/following-sibling::div//input").clear()
    driver.find_element_by_xpath(u"//label[text()=\"Smart Probe 别名\"]/following-sibling::div//input").send_keys(smart_name)
    driver.find_element_by_css_selector("button.btn.btn-primary.progress-button.save").click()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    driver = webdriver.Chrome()
    driver.set_window_size(3500, 1500)
    runit(driver)
    
    pass