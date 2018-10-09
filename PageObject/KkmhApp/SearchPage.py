#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 15:06
# @Author  : Kay
# @Site    : 
# @File    : SearchPage.py
# @Software: PyCharm Community Edition

from  Public.BasePage import  BasePage
from Public.Decorator import *
class SearchPage(BasePage):

    @teststep
    def SearchCancel_Click(self):
        self.d(text = "取消").click()