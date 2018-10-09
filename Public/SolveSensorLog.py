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
import  urllib
class SolveSensorLog:

    def getSensorLog(self,eventName,distinct_id,excption):
        Qury = ""
        for key  in  excption.keys():
            if Qury !="":
                Qury = Qury+ ","
            Qury = Qury+ key
        time.sleep(20)
        SensorData = {}
        url = 'http://saweb.quickcan.com/api/sql/query';



        qury = "select %s from events where event='%s'  and distinct_id='%s' order by time desc limit 1" % (
            Qury,eventName, distinct_id)

        data = {
            'project': 'kuaikan_test', 'token': '3d67271d47be74b33038aee703050c6e3b184a2fef274225bd229a3c8c98d0d8',
            'q': qury}
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data)
        req.add_header('Content-Type', "application/x-www-form-urlencoded")
        response = urllib.request.urlopen(req)
        resultqury = response.read().decode('utf-8')
        resultList = resultqury.split('\n')
        resultList1 = resultList[0]
        resultList2 = resultList[1]
        resultFirst  =  resultList1.split("\t")
        resultSecond  = resultList2.split("\t")
        SensorData = dict(zip(resultFirst,resultSecond))
        return SensorData


    def getSensorLogTest(self):

        time.sleep(5)
        EndTime = self.getSensorEndTime()
        EndTime = str(EndTime, encoding='utf-8')
        logcmd = r"adb logcat -v time | findstr AnalyticsMessages"
        Popen = subprocess.Popen(logcmd, stdout=subprocess.PIPE, shell=True)
        time.sleep(2)
        SensorData = []
        SensorDataSub = []
        isSartSave = False
        lines = ""
        while True:
            if lines != "":
                if  ("_flush_time"in lines )and (EndTime in lines):
                    L=lines
                    break;
            line = Popen.stdout.readline()
            lines = str(line, encoding='utf-8')
            if "}," in lines:
                isSartSave = False
            if "\"event\"" in lines:
                if len(SensorDataSub) > 0:
                    SensorDataSub.append(self.solveString(lines))
                    SensorData.append(SensorDataSub)
                    SensorDataSub = []
            if isSartSave == True:
                SensorDataSub.append(self.solveString(lines))
            if "\"properties\":{" in lines:
                isSartSave = True
        Popen.terminate()

        os.popen('taskkill /f /t /im cmd.exe')
        os.remove(r"D:\Test\AutoTestCase\Public\base.txt")
        return SensorData

    def  solveString(self,lines):
        solveString = re.findall(r"\".*,", lines)
        solveString  = "".join(solveString)
        return  solveString[:-1]







