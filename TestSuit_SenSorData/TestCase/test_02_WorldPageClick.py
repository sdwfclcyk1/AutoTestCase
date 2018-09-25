#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 14:46
# @Author  : Kay
# @Site    : 
# @File    : test_02_WorldPageClick.py
# @Software: PyCharm Community Edition
import unittest
from  Public.BasePage import BasePage
from  Public.JugementSensorData import JugementSensorData
from Public.Decorator import *
from PageObject.KkmhApp.WorldPage import  WorldPage
from Public.ReadConfig import ReadConfig
from  TestSuit_SenSorData.ExpectResult.WorldPageClick import  WorldClickExpection

event_name = ReadConfig().get_testEvent("世界页点击分布")
apkName = ReadConfig().get_pkg_name()
apkActivity = ReadConfig().get_pkg_activity()

class WorldPageClick(unittest.TestCase,BasePage):

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.set_fastinput_ime()
        cls.unlock_device()
        cls.d.app_start(apkName,apkActivity)
    @classmethod
    def  tearDown(cls):
        cls.d.app_stop(apkName)
    @testcase
    def test_02_WordClickAttention(self):
        WorldPage().World_Click()
        WorldPage().Attention_Click()
        server = WorldClickExpection()
        JugementSensorData.JugementData("test_01_AttentionClick", server)






