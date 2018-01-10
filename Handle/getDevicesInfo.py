# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/8 下午11:47
# Email: leiyong711@163.com

import json
import os
import subprocess


class Shell:
    def __init__(self):
        pass

    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


class Device:
    def __init__(self):
        pass

    @staticmethod
    def get_ios_devices():
        output = Shell.invoke('idevice_id -l')
        config_file = 'Config/ios_mapping.json'
        with open(config_file, 'r') as f:
            config = json.loads(f.read())

        if len(output) > 0:
            udids = output.strip('\n').split('\t')
            for udid in udids:
                doc = {}
                output = Shell.invoke('ideviceinfo -u %s -k ProductType' % udid)
                device_type = config[output.strip('\n')]
                brand = ''
                # -1表示找不到 0表示下标
                if device_type.find("iPhone") != -1:
                    brand = 'iPhone'
                elif device_type.find("iPad") != -1:
                    brand = 'iPad'
                elif device_type.find("iPod") != -1:
                    brand = 'iPod'

                outputVersion = Shell.invoke('ideviceinfo -u %s -k ProductVersion' % udid)
                doc['platformVersion'] = outputVersion.strip('\n')
                output = Shell.invoke('idevicename -u %s' % udid)
                doc['deviceName'] = output.strip('\n')
                doc['brand'] = brand
                doc['model'] = device_type
                doc['platformName'] = 'iOS'
                doc['udid'] = udid

        x = ["brand = %s\nmodel = %s\ndeviceName = %s\nplatformVersion = %s\nudid = %s\nplatformName = iOS"
             % (doc['brand'], doc['model'], doc['deviceName'], doc['platformVersion'], doc['udid'])]
        with open("Config/app.conf", "a") as f:  # 写出应用配置信息
            f.write("\n[phoneConf]\n")
            for i in x:
                f.write(i)


if __name__ == '__main__':
    d = Device()
    d.get_ios_devices
