# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 上午12:05
# Email: leiyong711@163.com

import zipfile
import biplist
import sys
import re
import os


class getApp:

    def __init__(self):
        filenames = os.listdir('Apps/')
        print filenames
        for i in range(len(filenames)):
            num = re.search(r'\.ipa$', filenames[i])
            if num:
                self.ipa_path = 'Apps/%s' % num.string
                # appLocation = num.string
                # print appLocation

    def analyze_ipa_with_plistlib(self):
        ipa_file = zipfile.ZipFile(self.ipa_path)
        plist_path = self.find_plist_path(ipa_file)
        plist_data = ipa_file.read(plist_path)
        plist_root = biplist.readPlistFromString(plist_data)
        self.print_ipa_info(plist_root)

    def print_ipa_info(self, plist_root):
        size = os.path.getsize(self.ipa_path)
        fileSize = round(size / 1024 / 1024.0, 2)  # 转大小单位
        fileSize = str(fileSize) + 'MB'

        x = ["applicationName = %s \nfileSize = %s \napplicationVersion = %s \nbundleId = %s\n" %
             (plist_root['CFBundleName'],fileSize, plist_root['CFBundleShortVersionString'], plist_root['CFBundleIdentifier'])]
        with open("config/app.conf", "w+") as f:  # 写出应用配置信息
            f.write("[baseconf]\n")
            for i in x:
                f.write(i)

    def find_plist_path(self, zip_file):
        name_list = zip_file.namelist()
        # print name_list
        pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
        for path in name_list:
            m = pattern.match(path)
            if m is not None:
                return m.group()




if __name__ == '__main__':
    a = getApp()
    a.analyze_ipa_with_plistlib()
