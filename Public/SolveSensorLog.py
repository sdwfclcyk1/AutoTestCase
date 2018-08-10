#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 21:15
# @Author  : Kay
# @Site    : 
# @File    : SolveSensorLog.py
# @Software: PyCharm Community Edition
import subprocess
import time
import os
import  re
class SolveSensorLog:

    def __init__(self,event= None):
        self.event = event

    def getSensorLog(self):
        logcmd = r"adb logcat -v time | findstr AnalyticsMessages > D:\Test\AutoTestCase\Public\base.txt"
        Popen = subprocess.Popen(logcmd, stdout=subprocess.PIPE, shell=True)
        time.sleep(5)
        Popen.terminate()
        os.popen('taskkill /f /t /im cmd.exe')
        time.sleep(5)
        return self.solveSensorLog()

    def solveSensorLog(self):
        SensorData = []
        SensorDataSub = []
        isSartSave = False
        file = open(r'D:\Test\AutoTestCase\Public\base.txt', encoding='utf-8')
        for lines in  file.readlines():
            if "}," in lines :
                isSartSave = False
            if "\"event\"" in lines:
                if len(SensorDataSub)>0:
                    SensorDataSub.append(self.solveString(lines))
                    SensorData.append(SensorDataSub)
                    SensorDataSub = []
            if isSartSave == True:
                SensorDataSub.append(self.solveString(lines))
            if "\"properties\":{" in lines:
                isSartSave = True
        file.close()
        os.popen('taskkill /f /t /im findstr.exe')
        time.sleep(1)
        os.remove(r"D:\Test\AutoTestCase\Public\base.txt")
        return  SensorData

    def  solveString(self,lines):
        solveString = re.findall(r"\".*,", lines)
        solveString  = "".join(solveString)
        return  solveString[:-1]









