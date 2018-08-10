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
from  Public.SolveSensorLog import  SolveSensorLog
from  Public.SenSorCheckPoint import SenSorCheckpoint
from TestSuit_SenSorData.ExpectResult.OpenApp import  OpenApp_Expection

event_name = ReadConfig().get_testEvent("打开App")

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
       cls.d.app_stop("com.kuaikan.comic")

   @testcase
   def test_01_coldapp(self):
        self.d.app_start("com.kuaikan.comic","com.kuaikan.comic.ui.LaunchActivity")
        SensorData = SolveSensorLog().getSensorLog()
        sensorResult = SenSorCheckpoint(SensorData,OpenApp_Expection().test_01_coldapp()).checkPoint()
        if len(sensorResult)>0:
            raise  Exception("OpenApp Error"+sensorResult)

   @testcase
   def test_01_hotapp(self):
       self.d.app_start("com.kuaikan.comic", "com.kuaikan.comic.ui.LaunchActivity")
       time.sleep(5)
       self.d.app_stop("com.kuaikan.comic")
       self.d.app_start("com.kuaikan.comic", "com.kuaikan.comic.ui.LaunchActivity")
       self.JugementSensorData("test_01_hotapp")


   @classmethod
   def JugementSensorData(self,functionName):
       SensorData = SolveSensorLog().getSensorLog()
       server = OpenApp_Expection()
       func = getattr(server,functionName)
       excption = func()
       sensorResult = SenSorCheckpoint(SensorData,excption).checkPoint()
       if len(sensorResult) > 0:
           raise Exception("OpenApp Error" + sensorResult)





