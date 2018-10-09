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
        resultString = ""
        for key in self.checkpoint.keys():
            isInSensorData = False
            value=""

            if key=="event":
                continue
            if self.checkpoint[key] is False:
                value = "false"
            elif self.checkpoint[key] is True:
                value = "true"
            else :
                value = self.checkpoint[key]
            if value  == self.sensorData[key.lower()] :
                isInSensorData = True
            if isInSensorData != True:
                resultString = resultString+"%s error,PleaseCheckOut"%(self.checkpoint[key])
        return  resultString
