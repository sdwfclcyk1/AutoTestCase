#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 15:01
# @Author  : Kay
# @Site    : 
# @File    : WorldPage.py
# @Software: PyCharm Community Edition
from  Public.BasePage import  BasePage
from Public.Decorator import *
class WorldPage(BasePage):

    @teststep
    def wait_page(self):
        try:
            if self.d(text='世界').wait(timeout=5):
                pass
            else:
                raise Exception('Not in WorldPage')
        except Exception:
            raise Exception('Not in WorldPage')

    @teststep
    def TabAttention_Click(self):
        self.d(text = "关注").click()

    @teststep
    def TabWorld_Click(self):
        self.d(text = "世界").click()

    @teststep
    def  TabSearch_Click(self):
        self.d(resourceId = "com.kuaikan.comic:id/btnSearch").click()

    @teststep
    def TabReacommend_Click(self):
        self.d(text = "推荐").click()

    @teststep
    def TabVComunit_Click(self):
        self.d(text = "V们").click()

    @teststep
    def TabSVideo_Click(self):
        self.d(text = "配音").click()

    @teststep
    #社区帖子详情点击
    def Post_Click(self):
        self.d(scrollable=True).scroll.to(resourceId ="com.kuaikan.comic:id/tv_summary")
        self.d(resourceId = "com.kuaikan.comic:id/tv_summary").click()
    @teststep
    #社区点击个人头像
    def  User_Click(self):
        self.d(resourceId = "com.kuaikan.comic:id/user_avatar").click()

    @teststep
    #社区点赞
    def WorldLike_Click(self):
        self.d(scrollable =True).scroll.to(resourceId = "com.kuaikan.comic:id/tv_like_count")
        self.d(resourceId = "com.kuaikan.comic:id/tv_like_count").click()

    @teststep
    def WorldReply_Click(self):
        self.d(scrollable=True).scroll.to(resourceId="com.kuaikan.comic:id/tv_comment_count")
        self.d(resourceId="com.kuaikan.comic:id/tv_comment_count").click()

