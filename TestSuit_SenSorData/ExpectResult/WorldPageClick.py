#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 15:41
# @Author  : Kay
# @Site    : 
# @File    : WorldPageClick.py
# @Software: PyCharm Community Edition

class WorldClickExpection:
    def test_01_AttentionClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName" :"关注Tab"
        }
        return  expection
    def  test_02_SearchClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "搜索"
        }
        return  expection
    def  test_03_ReacommendClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "推荐Tab"
        }
        return  expection
    def test_04_VComunitClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "V们Tab"
        }
        return expection
    def test_05_SVideoClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "配音Tab"
        }
    def test_06_PostClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "帖子详情"
        }
        return  expection

    def test_07_UserClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "个人详情"
        }
        return  expection

    def test_08_LikeClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "点赞"
        }
        return  expection

    def test_09_ReplyClick(self):
        expection = {
            "event": "WorldPageClick ",
            "ButtonName": "回复icon"
        }
        return  expection