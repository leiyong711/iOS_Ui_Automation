# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 上午12:47
# Email: leiyong711@163.com

from Handle.getAppInfo import getApp
from Handle.getDevicesInfo import Device
a = getApp()
a.analyze_ipa_with_plistlib()
d = Device()
d.get_ios_devices()