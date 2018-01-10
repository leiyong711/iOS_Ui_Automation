# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 下午6:14
# Email: leiyong711@163.com

import os


def msm():

    x = 1

    def sms():
        smsLog = os.popen('adb shell cat /sdcard/SMS/smsLog.txt').read()
        return smsLog.split("验证码是")[1]

    while x == 1:
        try:
            sm = sms()
            break
        except:
            x = 1
    os.popen('adb shell rm /sdcard/SMS/smsLog.txt')
    return sm

if __name__ == '__main__':
    print '验证码%s' % msm()
