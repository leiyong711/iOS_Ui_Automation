# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 上午1:11
# Email: leiyong711@163.com
import ConfigParser
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Handle.getAppInfo import getApp
from Handle.getDevicesInfo import Device

# 自动获取app与测试设备信息
a = getApp()
a.analyze_ipa_with_plistlib()
d = Device()
d.get_ios_devices()


# 获取config配置文件
def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = 'Config/app.conf'
    config.read(path)
    return config.get(section, key)


# 启动appium服务
class server:

    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = getConfig("phoneConf", "platformName")
        desired_caps['platformVersion'] = getConfig("phoneConf", "platformVersion")
        desired_caps['deviceName'] = getConfig("phoneConf", "deviceName")
        desired_caps['udid'] = getConfig("phoneConf", "udid")
        desired_caps['bundleId'] = getConfig("baseconf", "bundleId")
        # desired_caps['app'] = os.path.abspath('/test/HuiBao.ipa')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    print getConfig("baseconf", "applicationName")
    print getConfig("baseconf", "fileSize")
    print getConfig("baseconf", "applicationVersion")
    print getConfig("baseconf", "bundleId")

    print '-'*100
    print getConfig("phoneConf", "brand")
    print getConfig("phoneConf", "model")
    print getConfig("phoneConf", "deviceName")
    print getConfig("phoneConf", "platformVersion")
    print getConfig("phoneConf", "udid")
    print getConfig("phoneConf", "platformName")
