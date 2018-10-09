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
from PageObject.KkmhApp.WorldPage import *
from  PageObject.KkmhApp.SearchPage import *
from Public.ReadConfig import ReadConfig
from  TestSuit_SenSorData.ExpectResult.WorldPageClick import  WorldClickExpection

event_name = ReadConfig().get_testEvent("世界页点击分布")
apkName = ReadConfig().get_pkg_name()
distinct_id = ReadConfig().get_testUserID()
apkActivity = ReadConfig().get_pkg_activity()
Expection = WorldClickExpection()

class WorldPageClick(unittest.TestCase,BasePage):

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.set_fastinput_ime()
        cls.unlock_device()
        cls.d.app_start(apkName,apkActivity)
    @classmethod
    def  tearDown(cls):
        pass
        #cls.d.app_stop(apkName)
    @testcase
    @unittest.skip(u"无条件跳过")
    def test_01_WordClickAttention(self):
        WorldPage().TabWorld_Click()
        WorldPage().TabAttention_Click()
        JugementSensorData.JugementData("test_01_AttentionClick", Expection,event_name,distinct_id)

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_02_WorldClickSearch(self):
        WorldPage().TabSearch_Click()
        JugementSensorData.JugementData("test_02_SearchClick",Expection,event_name,distinct_id)
        SearchPage().SearchCancel_Click()

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_03_WorldClickReacommend(self):
        WorldPage().TabReacommend_Click()
        JugementSensorData.JugementData("test_03_ReacommendClick",Expection,event_name,distinct_id)

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_04_WorldClickVComunit(self):
        WorldPage().TabVComunit_Click()
        JugementSensorData.JugementData("test_04_VComunitClick",Expection,event_name,distinct_id)

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_05_WorldClickSVdieo(self):
        WorldPage().TabSVideo_Click()
        JugementSensorData.JugementData("test_05_SVideoClick",Expection,event_name,distinct_id)

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_06_WorldPostClick(self):
        #本用例只考虑V们页的帖子点击
        WorldPage().TabVComunit_Click()
        WorldPage().Post_Click()
        JugementSensorData.JugementData("test_06_PostClick",Expection,event_name,distinct_id)
        self.d.press("back")

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_07_WorldUserClick(self):
        #本用例只考虑V们页的个人详情点击
        WorldPage().TabVComunit_Click()
        WorldPage().User_Click()
        JugementSensorData.JugementData("test_07_UserClick", Expection, event_name, distinct_id)
        self.d.press("back")

    @unittest.skip(u"无条件跳过")
    @testcase
    def test_08_WorldLikeClick(self):
        #本用例只考虑V们页的点赞点击
        WorldPage().TabVComunit_Click()
        WorldPage().WorldLike_Click()
        JugementSensorData.JugementData("test_08_LikeClick",Expection,event_name,distinct_id)

    @testcase
    def test_09_WorldClickReply(self):
        # 本用例只考虑V们页的点赞点击
        WorldPage().TabVComunit_Click()
        WorldPage().WorldReply_Click()
        JugementSensorData.JugementData("test_09_ReplyClick",Expection,event_name,distinct_id)
        self.d.press("back")









