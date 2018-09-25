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
    def Attention_Click(self):
        self.d(text = "关注").click()
    @teststep
    def World_Click(self):
        self.d(text = "世界").click()


