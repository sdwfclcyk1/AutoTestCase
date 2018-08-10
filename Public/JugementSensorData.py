#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 16:53
# @Author  : Kay
# @Site    : 
# @File    : JugementSensorData.py
# @Software: PyCharm Community Edition

from  Public.SolveSensorLog import SolveSensorLog
from  Public.SenSorCheckPoint import SenSorCheckpoint

class JugementSensorData:
    @staticmethod
    def JugementData(functionName, server):
        SensorData = SolveSensorLog().getSensorLog()
        func = getattr(server, functionName)
        excption = func()
        sensorResult = SenSorCheckpoint(SensorData, excption).checkPoint()
        if len(sensorResult) > 0:
            raise Exception(" Error" + sensorResult)
