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