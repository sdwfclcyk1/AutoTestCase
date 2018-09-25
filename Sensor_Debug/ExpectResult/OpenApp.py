#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 17:51
# @Author  : Kay
# @Site    : 
# @File    : OpenApp.py
# @Software: PyCharm Community Edition、

class OpenApp_Expection:

    def test_01_coldapp(self):
        expection = {
            "event":"OpenApp",
            "FirstOpen":False,
            "OpenWay":1,
        }
        return  expection
    def test_01_hotapp(self):

        exception = {
            "event":"OpenApp",
            "FirstOpen":False,
            "OpenWay":1,
        }
        return  exception
# DeepLink 调起  linkeMe调起  AppToApp
    def test_01_OtherApp(self):
        exception = {

        }
        return  exception
#Push 调起应用
    def test_01_Push(self):
        exception = {

        }
        return  exception