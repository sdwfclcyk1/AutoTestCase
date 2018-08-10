#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 18:59
# @Author  : Kay
# @Site    :
# @File    : test_01_openapp.py
# @Software: PyCharm Community Edition

import uiautomator2 as u2
import unittest
from Public.Decorator import *
from Public.BasePage import BasePage
from Public.ReadConfig import ReadConfig
from  Public.JugementSensorData import JugementSensorData
from TestSuit_SenSorData.ExpectResult.OpenApp import  OpenApp_Expection

event_name = ReadConfig().get_testEvent("打开App")
apkpage = ReadConfig().get_pkg_name()
apkActivity = ReadConfig().get_pkg_activity()

class OpenApp(unittest.TestCase,BasePage):

   @classmethod
   @setupclass
   def setUpClass(cls):
        cls.set_fastinput_ime()
        cls.unlock_device()
        cls.d.app_stop_all()

   @classmethod
   @setupclass
   def tearDownClass(cls):
       cls.d.app_stop(apkpage)

   @testcase
   def test_01_coldapp(self):
        self.d.app_start(apkpage,apkActivity)
        server = OpenApp_Expection()
        JugementSensorData.JugementData("test_01_coldapp",server)

   @testcase
   def test_01_hotapp(self):
       self.d.app_start(apkpage, apkActivity)
       time.sleep(5)
       self.d.app_stop(apkpage)
       self.d.app_start(apkpage, apkActivity)
       server = OpenApp_Expection()
       JugementSensorData.JugementData("test_01_hotapp",server)






