#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject import LoginPage
import unittest

from Public.ReadConfig import ReadConfig
apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()


class apk_install(unittest.TestCase, BasePage):
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.set_fastinput_ime()
        cls.unlock_device()
        cls.d.app_stop_all()


    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.github.android_app_bootstrap")

    @testcase
    def test_01_install_apk(self):
        '''安装启动android_app_bootstrap'''
        self.d.app_install(apk_url)
        self.d.app_start(pkg_name)

        time.sleep(3)
        LoginPage.LoginPage().wait_page()

    @testcase
    def test_03_screenshot(self):
        '''手动截图测试'''
        self.screenshot()
        self.d.open_identify()
        self.screenshot()

    @testcase
    def test_02_fail(self):
        '''异常处理'''
        self.d(text='Login').click()
        print('手动截图一张')
        self.screenshot()

    @testcase
    def test_04_error(self):
        '''错误处理'''
        print('手动出错')
        raise Exception('手动ERROR!!!!!!!')


