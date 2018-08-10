#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 18:04
# @Author  : Kay
# @Site    : 
# @File    : SenSorCheckPoint.py
# @Software: PyCharm Community Edition

class SenSorCheckpoint:
    def __init__(self,sensorData,checkpoint):
        self.sensorData = sensorData
        self.checkpoint = checkpoint

    def checkPoint(self):
        LocalSenSorData = []
        for i  in range(0, self.sensorData.__len__())[::-1]:
            if "\"event\":\"%s\""%(self.checkpoint["event"]) in self.sensorData[i]:
                LocalSenSorData = self.sensorData[i];
                break
        resultString = ""
        for key in self.checkpoint.keys():
            isInSensorData = False
            value=""
            for i in LocalSenSorData:
                if key=="event":
                    break
                if self.checkpoint[key] is False:
                    value = "false"
                elif self.checkpoint[key] is True:
                    value = "true"
                else :
                    value = self.checkpoint[key]
                if "\"%s\":%s"%(key,value)  in i :
                    isInSensorData = True
            if (isInSensorData != True)and(key!="event"):
                resultString = resultString+"%s error,PleaseCheckOut"%(key)
        return  resultString
