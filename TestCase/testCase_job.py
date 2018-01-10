# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: iOS_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/9 下午5:48
# Email: leiyong711@163.com

import os
import time
import unittest
from Handle.positioning import Element
el = Element()


class Dtt(unittest.TestCase):
    """登录用例"""
    driver = el.driver

    def job(self, jobValue):
        el.localizeName(u'首页').click()
        el.findLocal(u"请点击描述您的需求")
        el.LocalizeDesc(u"请点击描述您的需求").click()
        el.localizeName(u'详细描述你的任务要求，需要解决什么问题（不能少于10个字）').send_keys(jobValue)

    def test_001(self):
        """任务要求为空，发布任务"""
        self.job('')
        el.LocalizeDesc(u'完成').click()
        self.assertTrue(el.toCompareDesc(u'任务要求'))

    def test_002(self):
        """任务要求少于10个字，发布任务"""
        self.job(u'我就发布一个任务测')
        el.LocalizeDesc(u'完成').click()
        self.assertTrue(el.toCompareDesc(u'任务要求'))

    def test_003(self):
        """任务要求大于10个字，不选择技能标签，发布任务"""
        self.job(u'我就发布一个任务测试一下')
        el.LocalizeDesc(u'外墙清洗').click()
        el.LocalizeDesc(u'完成').click()
        self.assertTrue(el.toCompareDesc(u'任务要求'))

    def test_004(self):
        """任务要求大于10个字，选择技能标签，发布任务"""
        self.job(u'我就发布一个任务测试一下')
        el.LocalizeDesc(u'外墙清洗').click()
        el.LocalizeDesc(u'完成').click()
        self.assertTrue(el.toCompareDesc(u'您的任务发布成功, 惠包客服将会尽快与您联系'))
        el.LocalizeDesc('navi back white image').click()
        self.assertTrue(el.to_compareName(u'首页'))



