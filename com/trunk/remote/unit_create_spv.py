# -*- coding: utf-8 -*-
'''
Created on 2015年12月22日

@author: Palmer.Piao
'''
import unittest,time,csv,os,sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import json
import datetime
from time import strftime
# from com.bco.init.createLCV import driver



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
        result[row[0]]=row[1]#value存成string
    csvfile.close()
    return result

def waitCssElement(csslocator):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, csslocator)))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,csslocator)))

def inputTextByXpathToElement(driver,xpath,text):
    driver.find_element_by_xpath(xpath).clear()
    driver.find_element_by_xpath(xpath).send_keys(text)
def hover(driver,element):
    ActionChains(driver).move_to_element(element).perform()
def drag_to_target(driver,source,target):
    ActionChains(driver).drag_and_drop(source, target).perform()

def setIp(csslocator,ips):
    driver.find_element_by_css_selector(csslocator).clear()
    
    for index,ip in enumerate(ips.split(",")):
        print ip
        if index == 0:
            pass
        else:
            ActionChains(driver).key_down(Keys.ENTER).perform()
        driver.find_element_by_css_selector(csslocator).send_keys(ip)
        print "index = ",index
        
            
        
def setPort(csslocator,ports):
    driver.find_element_by_css_selector(csslocator).clear()
    for index,port in enumerate(ports.split(",")):
        print port
        if index == 0:
            pass
        else:
            ActionChains(driver).key_down(Keys.ENTER).perform()
        driver.find_element_by_css_selector(csslocator).send_keys(port)
        
        
    
def saveIpPort():
    driver.find_element_by_css_selector("button.btn-img.btn-img-save.btn-tip.tooltip-save").click()

def  createSPV(spvname):
    add_btns = driver.find_elements_by_css_selector("div.view-add-icon.glyphicon.glyphicon-add")
#     time.sleep(4)
# #     for i in add_btns:
# #         print i
        
    if len(add_btns)==3:
        add_btns[2].click()
    
    inputTextByXpathToElement(driver,"//input",spvname+strftime("%H:%M:%S",time.localtime()))
    driver.find_element_by_css_selector("button.btn.btn-primary.progress-button.save").click()

def setSmartOption(smart_point):
    #    打开smartprobe point编辑窗口
    smart_point.click()
    #    选择smartprobe端口
    linka = driver.find_element_by_css_selector("div:not([style]).crossflow-ztip-group a")
    ActionChains(driver).click_and_hold(linka).perform()
     
    time.sleep(1)
    ActionChains(driver).release(linka).perform()
    time.sleep(1)
#    选择第二个smartprobe ip
    ActionChains(driver).key_down(Keys.DOWN).perform()
#     need update
#     time.sleep(1)
#     ActionChains(driver).key_down(Keys.DOWN).perform() 
    time.sleep(1)
    ActionChains(driver).key_down(Keys.ENTER).perform()
    ActionChains(driver).release() 
    
    driver.find_element_by_css_selector("button.btn-img.btn-img-save.btn-tip.tooltip-save").click()

def applySPV():
    driver.find_element_by_css_selector("button.btn-img.btn-img-create.btn-tip").click()
#     time.sleep(10)
#     wait = WebDriverWait(driver, 10)
#     element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.crossflow-button-cancel.crossflow-button.pull-right.btn-img-cancel')))
#     element.click()
    waitCssElement("div.crossflow-button-cancel.crossflow-button.pull-right.btn-img-cancel")
    driver.find_element_by_css_selector("div.crossflow-button-cancel.crossflow-button.pull-right.btn-img-cancel").click()
    time.sleep(1)

def setTCP(jsonStr):
    tcpType = "default"
    try:
        tcpType = jsonStr["tcpType"]
    except Exception as err:
        print err," is not set, use default -> tcp short connect type"
        pass
    if tcpType == "long":
        driver.find_element_by_css_selector("ul.nav.crossflow-ztip-nav>li:nth-child(2)").click()
        driver.find_element_by_css_selector("div.crossflow-ztip-group.active>label:nth-child(2)").click()
        pass
    elif tcpType == "async":
        driver.find_element_by_css_selector("ul.nav.crossflow-ztip-nav>li:nth-child(2)").click()
        driver.find_element_by_css_selector("div.crossflow-ztip-group.active>label:nth-child(3)").click()
        pass
    else:
        pass
    
    
def MoreDroppableDiv():
    waitCssElement("div.slide-container.style-b>div.right")
    right_expand_icon = driver.find_element_by_css_selector("div.slide-container.style-b>div.right")
    ActionChains(driver).click_and_hold(right_expand_icon).perform()
    time.sleep(4)
    ActionChains(driver).release(right_expand_icon).perform()
    left_expand_icon = driver.find_element_by_css_selector("div.slide-container.style-b>div.left")
    ActionChains(driver).click_and_hold(left_expand_icon).perform()
    time.sleep(4)
    ActionChains(driver).release(left_expand_icon).perform()
    

def CreateLink(str,direction):
    client = driver.find_element_by_xpath("//div[@name='client']/div")
    app1 = driver.find_element_by_xpath("//div[@name='server1']/div")
    point_right = driver.find_element_by_xpath("//div[@name='point_right']/div")
    smart_probe = driver.find_element_by_xpath("//div[@name='smart_probe']/div")
#     str = json.loads('{"type":"client", "ipport":{"ip":"0.0.0.0,0.0.0.1", "port":"0-65535"}}')
    jsonStr = json.loads(str)
    type = jsonStr["type"]
    Lip = jsonStr["ipport"]["Lip"]
    Rip = jsonStr["ipport"]["Rip"]
    Lport = jsonStr["ipport"]["Lport"]
    Rport = jsonStr["ipport"]["Rport"]
    side = direction
    global targets_number
    targets = driver.find_elements_by_css_selector("div[style*='top: 85'].vbox.ui-droppable")

    if type == "client":
        object = driver.find_element_by_xpath("//div[@name='client']/div")
        drag_to_target(driver, object, targets[targets_number])
        targets_number += 1
    elif type == "app1":
        object = driver.find_element_by_xpath("//div[@name='server1']/div")
        drag_to_target(driver, object, targets[targets_number])
        targets_number += 1
    print targets_number
    global component_number
    if side == "right" :
        directObj = driver.find_element_by_xpath("//div[@name='point_right']/div")
        components = driver.find_elements_by_css_selector("div.component-wrapper")
        right_point = components[component_number].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable")
        drag_to_target(driver, directObj, right_point)
        interface_image = components[component_number].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable>img")
        component_number += 1
        interface_image.click()
        setIp("div.ztip-inner.active textarea[name='ips']",Rip)
        setPort("div.ztip-inner.active textarea[name='ports']", Rport)
        saveIpPort()
#         time.sleep(3)
    elif side == "left":
        directObj = driver.find_element_by_xpath("//div[@name='point_right']/div")
        components = driver.find_elements_by_css_selector("div.component-wrapper")
        left_point = components[component_number].find_element_by_css_selector("div[side='left'].connprop-holder.ui-droppable")
        drag_to_target(driver, directObj, left_point)
        interface_image = components[component_number].find_element_by_css_selector("div[side='left'].connprop-holder.ui-droppable>img")
        interface_image.click()
        setIp("div.ztip-inner.active textarea[name='ips']",Lip)
        setPort("div.ztip-inner.active textarea[name='ports']", Lport)
        setTCP(jsonStr)
        saveIpPort()
#         time.sleep(3)
        previous_component_right_point = components[component_number-1].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable")
        drag_to_target(driver, previous_component_right_point, left_point)
#         time.sleep(1)
        # # 由于click事件不能让smartprobe接受方块div显示，所以做了个hack方式的drag，从原地拖拽到原地，让div显示
        drag_to_target(driver, smart_probe, smart_probe)
#         time.sleep(1)
        target_smart_slot = components[component_number].find_element_by_css_selector("div[side='left'].capturer-holder.ui-droppable.active")
        drag_to_target(driver, smart_probe, target_smart_slot)
#         time.sleep(1)
        smart_image = components[component_number].find_element_by_css_selector("div[side='left'].capturer-holder.ui-droppable img")
        setSmartOption(smart_image)
        component_number += 1
    else:
        directObj = driver.find_element_by_xpath("//div[@name='point_right']/div")
        components = driver.find_elements_by_css_selector("div.component-wrapper")
        right_point = components[component_number].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable")
        drag_to_target(driver, directObj, right_point)
        right_interface_image = components[component_number].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable>img")
        right_interface_image.click()
        setIp("div.ztip-inner.active textarea[name='ips']",Rip)
        setPort("div.ztip-inner.active textarea[name='ports']", Rport)
        saveIpPort()
#         time.sleep(1)
        left_point = components[component_number].find_element_by_css_selector("div[side='left'].connprop-holder.ui-droppable")
        drag_to_target(driver, directObj, left_point)
        left_interface_image = components[component_number].find_element_by_css_selector("div[side='left'].connprop-holder.ui-droppable>img")
        left_interface_image.click()
        setIp("div.ztip-inner.active textarea[name='ips']",Lip)
        setPort("div.ztip-inner.active textarea[name='ports']", Lport)
        setTCP(jsonStr)
        saveIpPort()
#         time.sleep(1)
        previous_component_right_point = components[component_number-1].find_element_by_css_selector("div[side='right'].connprop-holder.ui-droppable")
        drag_to_target(driver, previous_component_right_point, left_point)
        # # 由于click事件不能让smartprobe接受方块div显示，所以做了个hack方式的drag，从原地拖拽到原地，让div显示
        drag_to_target(driver, smart_probe, smart_probe)
#         time.sleep(1)
        target_smart_slot = components[component_number].find_element_by_css_selector("div[side='left'].capturer-holder.ui-droppable.active")
        drag_to_target(driver, smart_probe, target_smart_slot)
#         time.sleep(1)
        smart_image = components[component_number].find_element_by_css_selector("div[side='left'].capturer-holder.ui-droppable img")
        setSmartOption(smart_image)
        component_number += 1

def createJLSB():
#     建连失败
    waitCssElement("div.view-add-bg")
#     spv_confs = driver.find_elements_by_xpath("//div[@viewtype='spv']")
#     print len(spv_confs)
    createSPV(u"建连失败")
#     if not spv_confs:
#         createSPV(u"建连失败")
#     else:
# # for testing, use existed spv         
#         for spv_conf in spv_confs:
#             hover(driver,spv_conf)
#             print spv_conf
#             print spv_conf.find_element_by_xpath("//button[@name='setting']").get_attribute("url")
# #有些隐藏的element，需要先让其visible后才能触发点击，否则报错,还要写全路径
# #             spv_conf.find_element_by_xpath("//div[@viewtype='spv']//button[@name='setting']").click()
#             spv_conf.find_element_by_name("setting").click()
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"68.45.134.187,68.164.173.62", "Rport":"0-65535"}}'
    node2='{"type":"app1", "ipport":{"Lip":"172.16.1.10", "Lport":"26452","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()
    
    
def createYCQR():
#     延迟确认
    waitCssElement("div.view-add-bg")
    createSPV(u"延迟确认")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"144.0.16.181,144.0.16.183", "Rport":""}}'
    node2='{"type":"app1","tcpType":"async","ipport":{"Lip":"144.255.249.131,144.255.249.132", "Lport":"21127,21128,23127,23128","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()    

def createCLJCC():
#     长连接重传
    waitCssElement("div.view-add-bg")
    createSPV(u"长连接重传")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"", "Rport":""}}'
    node2='{"type":"app1", "tcpType":"long","ipport":{"Lip":"10.253.71.12", "Lport":"23374","Rip":"197.2.0.4", "Rport":""}}'
    node3='{"type":"app1", "tcpType":"long","ipport":{"Lip":"9.234.6.23", "Lport":"47904","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"both")
    CreateLink(node3,"left")
    applySPV()  

def createLCK():
#     零窗口
    waitCssElement("div.view-add-bg")
    createSPV(u"零窗口")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"10.0.52.164", "Rport":""}}'
    node2='{"type":"app1", "ipport":{"Lip":"61.8.0.17", "Lport":"0-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()  

def createCLJRST():
#    长连接RST，gre回放， default_0_20160121153800.pcap 1分钟

    waitCssElement("div.view-add-bg")
    createSPV(u"长连接RST")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"172.16.14.138", "Rport":"38611-65535"}}'
    node2='{"type":"app1","tcpType":"long", "ipport":{"Lip":"172.16.14.137", "Lport":"8031-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()
    
def createFWDBCC():
#     服务端丢包重传 

    waitCssElement("div.view-add-bg")
    createSPV(u"服务端丢包重传")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"10.1.10.26", "Rport":"0-65535"}}'
    node2='{"type":"app1","ipport":{"Lip":"10.1.15.98", "Lport":"0-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()

def createStanderdSPV():
#     回放tap_1_znap.pcap 

    waitCssElement("div.view-add-bg")
    createSPV(u"SPV")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"144.7.22.11,144.7.26.13", "Rport":"0-65535"}}'
    node2='{"type":"app1","ipport":{"Lip":"144.7.24.12,144.7.24.14", "Lport":"0-65535","Rip":"", "Rport":""}}'
    node3='{"type":"app1","ipport":{"Lip":"144.255.1.1/16,144.7.66.1/24,144.24.64.1/24,144.80.1.1/24,144.144.64.1/24", "Lport":"0-65535","Rip":"", "Rport":""}}'
    node4='{"type":"app1","ipport":{"Lip":"144.7.24.12", "Lport":"0-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"both")
    CreateLink(node3,"both")
    CreateLink(node4,"left")
    applySPV()
    
def createPerformanceSPV():
#     回放tap_1_znap.pcap 

    waitCssElement("div.view-add-bg")
    createSPV(u"Performance_SPV")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"", "Rport":""}}'
    node2='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"144.255.248.129", "Rport":"0-65535"}}'
    node3='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"144.255.248.129", "Rport":"0-65535"}}'
    node4='{"type":"app1","ipport":{"Lip":"144.7.26.13", "Lport":"0-65535","Rip":"144.255.249.131", "Rport":"0-65535"}}'
    node5='{"type":"app1","ipport":{"Lip":"144.7.26.13", "Lport":"0-65535","Rip":"144.255.249.131", "Rport":"0-65535"}}'
    node6='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"144.255.249.132", "Rport":"0-65535"}}'
    node7='{"type":"app1","ipport":{"Lip":"144.7.26.13", "Lport":"0-65535","Rip":"144.255.249.132", "Rport":"0-65535"}}'
    node8='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"144.255.248.116", "Rport":"0-65535"}}'
    node9='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"144.255.248.116", "Rport":"0-65535"}}'
    node10='{"type":"app1","ipport":{"Lip":"144.7.26.13", "Lport":"0-65535","Rip":"144.255.248.115", "Rport":"0-65535"}}'
    node11='{"type":"app1","ipport":{"Lip":"144.7.22.11", "Lport":"0-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"both")
    CreateLink(node3,"both")
    CreateLink(node4,"both")
    CreateLink(node5,"both")
    CreateLink(node6,"both")
    CreateLink(node7,"both")
    CreateLink(node8,"both")
    CreateLink(node9,"both")
    CreateLink(node10,"both")
    CreateLink(node11,"left")
    applySPV()

def createTest():
#     default_0_20160121153800.pcap 1分钟

    waitCssElement("div.view-add-bg")
    createSPV(u"test")
    node1='{"type":"client", "ipport":{"Lip":"", "Lport":"","Rip":"172.16.14.138", "Rport":"38611-65535"}}'
    node2='{"type":"app1", "tcpType":"long","ipport":{"Lip":"172.16.14.137", "Lport":"8031-65535","Rip":"", "Rport":""}}'
    CreateLink(node1,"right")
    CreateLink(node2,"left")
    applySPV()


def resetConf():
    global targets_number,component_number
    targets_number = 0
    component_number = 0
    driver.get(base_url+"/zh-cn/manager/views/")
    
    
def runit(webdriver):
    try:
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
#         print dirname, filename
    except Exception as Err:
        dirname = os.getcwd()
        pass
    
    csvpath = os.path.abspath(os.path.join(dirname,"..","testdata","BCO.csv"))

#     csvpath = dirname+"/../../../sources/BCO.csv"
    # print sys.argv[1]
    result=parseCsv(csvpath)
    
    
    
    global base_url,driver,targets_number,component_number
    base_url = result.get("base_url")
    targets_number = 0
    component_number = 0
    
    driver = webdriver
    driver.get(base_url+"/zh-cn/accounts/login/?next=/zh-cn/manager/views/")
    login(driver,result)
    createJLSB()
    resetConf()
    createYCQR()
    resetConf()
    createCLJCC()
    resetConf()
    createLCK()
    resetConf()
    createCLJRST()
    resetConf()
    createFWDBCC()
    resetConf()
    createStanderdSPV()
    resetConf()
    createPerformanceSPV()
    
    
# if __name__ == '__main__':
#     driver = webdriver.PhantomJS()
#     driver.set_window_size(2400,1000)
#     runit(driver)
#     driver.quit()
