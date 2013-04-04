#! /usr/bin/python
import time
from datetime import datetime, timedelta
from win32com.client import Dispatch

class OSIPiConnection:
	def __init__(self, username_, password_, server_ = ""):
		self.pisdk = Dispatch('PISDK.PISDK')
		self.server = self.pisdk.Servers(server_)
		self.conn = Dispatch('PISDKDlg.Connections')
		self.conn.Login(self.server, username_, password_, 1, 0)
		
	def __findPiPoint(self, name_):
		return self.server.PIPoints[name_]
		
	def currentValue(self, tagName_):
		if not tagName_.startswith("HVO.ENV."):
			tagName_ = "HVO.ENV." + tagName_
	
		point = self.__findPiPoint(tagName_)
		
		val = point.Data.Snapshot
		if val.IsGood:
			try:
				return round(val.Value, 2)
			except:
				pass
		return -1.0

p = OSIPiConnection("pidemo", "", "hvspi")
while True:
	value = p.currentValue("HVO.ENV.KNODLRS_BARNOWL_CH01_IMPSP_W")
	print value
	time.sleep(5)
#tdMax = timedelta(minutes=15)
#piTimeStart = Dispatch('PITimeServer.PITimeFormat')
#piTimeEnd = Dispatch('PITimeServer.PITimeFormat')
#piTimeStart.InputString = '08-25-2009 00:00:00'
#piTimeEnd.InputString = '08-25-2009 23:59:59'
#sampleAsynchStatus = Dispatch('PISDKCommon.PIAsynchStatus')
#samplePoint = myServer.PIPoints['HVO.ENV.HVOMET__WIND_SPEED']
#sampleValues = samplePoint.Data.Summaries2(piTimeStart,piTimeEnd,'1h',5,0,sampleAsynchStatus)
#t0 = datetime.now()
#while True:
#    try:
#        valsum = sampleValues("Average").Value # retrieve the value
#        break  # it will get out of infinite loop when there is no error
#    except:  # it failed because server needs more time
#        td = datetime.now() - t0
#        if td > tdMax:
#            print "It is taking so long to get PI data ! Exiting now ...."
#            exit(1)
#        time.sleep(3)
#i = 1
#while i < valsum.Count+1:
#    print valsum(i).Value, valsum(i).ValueAttributes('Percentgood').Value
#    i += 1
