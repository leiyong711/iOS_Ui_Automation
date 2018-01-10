# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 下午5:47
# Email: leiyong711@163.com

import os
import time
import unittest
from Handle.positioning import Element
el = Element()


class Dtt(unittest.TestCase):
    """登录用例"""
    driver = el.driver

    def phoneLogin(self, phone, passwd):
        el.localizeName(u'请输入您的手机号码').clear()
        el.localizeName(u'请输入您的手机号码').send_keys(phone)
        el.localizeName(u'验证码').send_keys(passwd)
        el.localizeName(u'登录').click()

    def test_001(self):
        """空手机号&空密码登录"""
        time.sleep(1)
        el.localizeName('login select phone').click()
        self.phoneLogin('', '')
        self.assertTrue(el.to_compareName(u'首页'))

    def test_002(self):
        """空手机号登录"""
        self.phoneLogin('', '')
        self.assertTrue(el.to_compareName(u'首页'))

    def test_003(self):
        """空验证码登录"""
        self.phoneLogin('18682182291', '')
        self.assertTrue(el.to_compareName(u'首页'))

    def test_004(self):
        """正确的手机号与验证码登录"""
        self.phoneLogin('18682182291', '5555')
        time.sleep(1)
        self.assertTrue(el.to_compareName(u'首页'))


if __name__=='__main__':
    # a = Dtt()
    # a.phoneLogin('18682182291', '5555')
    suite = unittest.TestLoader().loadTestsFromTestCase(Dtt)
    unittest.TextTestRunner(verbosity=2).run(suite)

