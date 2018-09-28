#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 17:19
# @Author  : Kay
# @Site    : 
# @File    : Test.py
# @Software: PyCharm Community Edition
import threading
class Test():
    def test(self):
        def worker():
            print("worker")
        t= threading.Thread(target=worker)
        t.start()
if __name__ == '__main__':
    test = test().test()