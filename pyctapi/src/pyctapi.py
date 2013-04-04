#! /usr/bin/python
#
# File: pyctapi.py
# Author: Mitchell Gayner
# Date: 06/08/2009
#
# Desc: 
#  	Wrapper for Citect CTAPI dll
#	Compatible with Citect V6.1 DLLs
#
#	You must have the following DLLs:
#		- CiDebugHelp.dll
#		- Ct_ipc.dll
#		- CtApi.dll
#		- CtEng32.dll
#		- CtRes32.DLL
#		- CtUtil32.dll
#
import platform
from ctypes import * 
import sys

if platform.system() != "Windows":
    raise OSError

class pyCtApi:
	def __init__(self, dllPath_ = "C:/citect/bin/"):
		#Load required DLLs
		CDLL(dllPath_ + '/CiDebugHelp')
		CDLL(dllPath_ + '/CtUtil32')
		CDLL(dllPath_ + '/Ct_ipc')
		self.__libc = CDLL(dllPath_ + '/CtApi')
		self.__cn = None # Create connection object

	def Open(self, address_, username_, password_, mode_ = 0):
		"Open connection to running citect process"
		if self.__cn != None:
			print "Already connected"
			return
		self.__cn = windll.CtApi.ctOpen(address_, username_, password_, 2)
		
	def Close(self):
		"Close connection to running citect process"
		ct = windll.CtApi.ctClose(self.__cn)
		self.__cn = None
		
	def Connected(self):
		if self.__ExecCicode("Version(0)") != "":
			return True
		return False

	def TagReadInt(self, tagName_):
		"Read tag from Citect and covert to int"
		str = self.__TagRead(tagName_)
		#try:
		return int(str)
		#except:
		return -1
	
	def TagReadFloat(self, tagName_):
		"Read tag from Citect and covert to float"
		str = self.__TagRead(tagName_)
		#try:
		return float(str)
		#except:
		return -1
		
	def TagReadStr(self, tagName_):
		"Read tag from Citect and covert to string"
		str = self.__TagRead(tagName_)
		return str
		
	def TagWrite(self, tagName_, value_):
		"Write value to Citect tag"
		ok = self.__TagWrite(tagName_, str(value_))
		return ok
	
	def ExecuteCicode(self, function_):
		return self.__ExecCicode(function_)
	
	def __TagRead(self, tagName_):
		"PRIVATE: Read tag from Citect tag"
		f = create_string_buffer('\000' * 32)
		ok = windll.CtApi.ctTagRead(self.__cn, tagName_, byref(f), sizeof(f))
		return f.value
		
	def __TagWrite(self, tagName_, value_):
		"PRIVATE: Write value to Citect tag"
		ok = windll.CtApi.ctTagWrite(self.__cn, tagName_, value_)
		return ok
		
	def __ExecCicode(self, function_, hWin_=0, nMode_=0):
		f = create_string_buffer('\000' * 32)
		ok = windll.CtApi.ctCicode(self.__cn, function_, hWin_, nMode_, byref(f), sizeof(f), None)
		return f.value
	
	
	
# TODO LIST:
'''DONE extern	HANDLE	CTAPICALL	ctOpen(LPCSTR,LPCSTR,LPCSTR,DWORD);				/* Open CTAPI interface		*/'''
# extern	BOOL	CTAPICALL	ctOpenEx(LPCSTR,LPCSTR,LPCSTR,DWORD,HANDLE);
# extern	HANDLE	CTAPICALL	ctClientCreate();
# extern	BOOL	CTAPICALL	ctClientDestroy(HANDLE);
'''DONE extern	BOOL	CTAPICALL	ctClose(HANDLE);						/* Close CTAPI interface	*/'''
# extern	BOOL	CTAPICALL	ctCloseEx(HANDLE, BOOL);
# extern	BOOL	CTAPICALL	ctCancelIO(HANDLE,CTOVERLAPPED*);				/* cancel pending I/O		*/
'''DONE extern	DWORD	CTAPICALL	ctCicode(HANDLE,LPCSTR,DWORD,DWORD,LPSTR,DWORD,CTOVERLAPPED*);	/* execute cicode		*/'''
# extern	BOOL	CTAPICALL	ctPointWrite(HANDLE,HANDLE,void*,DWORD,CTOVERLAPPED*);		/* write to point handle	*/
# extern	BOOL	CTAPICALL	ctPointRead(HANDLE,HANDLE,void*,DWORD,CTOVERLAPPED*);		/* read from point handle	*/
# extern	HANDLE	CTAPICALL	ctTagToPoint(HANDLE,LPCSTR,DWORD,CTOVERLAPPED*);		/* convert tag into point handle*/
# extern	BOOL	CTAPICALL	ctPointClose(HANDLE,HANDLE);					/* free a point handle		*/
# extern	HANDLE	CTAPICALL	ctPointCopy(HANDLE);						/* copy a point handle		*/
# extern	BOOL	CTAPICALL	ctPointGetProperty(HANDLE,LPCTSTR,void*,DWORD,DWORD*,DWORD);	/* get point property		*/
# extern	DWORD	CTAPICALL	ctPointDataSize(HANDLE);					/* size of point data buffer	*/
# extern	DWORD	CTAPICALL	ctPointBitShift(HANDLE);					/* calculate bit shift offset	*/
# extern	BOOL	CTAPICALL	ctPointToStr(HANDLE,BYTE*,DWORD,BYTE*,DWORD,DWORD);		/* format point data to string	*/
# extern	BOOL	CTAPICALL	ctStrToPoint(HANDLE,LPCSTR,DWORD,BYTE*,DWORD,DWORD);		/* format string data into point*/
'''DONE extern	BOOL	CTAPICALL	ctTagWrite(HANDLE,LPCSTR,LPCSTR);				/* write to tag			*/'''
'''DONE extern	BOOL	CTAPICALL	ctTagRead(HANDLE,LPCSTR,LPSTR,DWORD);				/* read from tag		*/'''
# extern	BOOL	CTAPICALL	ctEngToRaw(double*,double,CTSCALE*,DWORD);			/* scale from eng to raw	*/
# extern	BOOL	CTAPICALL	ctRawToEng(double*,double,CTSCALE*,DWORD);			/* scale from raw to eng	*/
# extern	BOOL	CTAPICALL	ctGetOverlappedResult(HANDLE,CTOVERLAPPED*,DWORD*,BOOL);	/* get overlapped result	*/
# extern	BOOL	CTAPICALL	ctEngToRaw(double*,double,CTSCALE*,DWORD);			/* scale from eng to raw	*/
# extern	BOOL	CTAPICALL	ctRawToEng(double*,double,CTSCALE*,DWORD);			/* scale from raw to eng	*/
# extern	HANDLE	CTAPICALL	ctFindFirst(HANDLE,LPCTSTR,LPCTSTR,HANDLE*,DWORD);		/* initiate a search		*/
# extern	BOOL	CTAPICALL	ctFindNext(HANDLE,HANDLE*);					/* get the next search item	*/
# extern	BOOL	CTAPICALL	ctFindPrev(HANDLE,HANDLE*);					/* get the prev search item	*/
# extern	DWORD	CTAPICALL	ctFindScroll(HANDLE,DWORD,LONG,HANDLE*);			/* scroll to search item	*/
# extern	BOOL	CTAPICALL	ctFindClose(HANDLE);						/* close a search		*/
# extern	LONG	CTAPICALL	ctFindNumRecords(HANDLE);					/* get the total number of records in the search */
# extern	BOOL	CTAPICALL	ctGetProperty(HANDLE,LPCTSTR,void*,DWORD,DWORD*,DWORD);		/* get a named property		*/
# extern	HANDLE	CTAPICALL	ctListNew(HANDLE,DWORD);					/* create poll list		*/
# extern	BOOL	CTAPICALL	ctListFree(HANDLE);						/* free poll list		*/
# extern	HANDLE	CTAPICALL	ctListAdd(HANDLE,LPCSTR);					/* add tag to poll list		*/
# extern	BOOL	CTAPICALL	ctListDelete(HANDLE);						/* delete tag from poll list	*/
# extern	BOOL	CTAPICALL	ctListRead(HANDLE,CTOVERLAPPED*);				/* read poll list		*/
# extern	BOOL	CTAPICALL	ctListWrite(HANDLE,LPCSTR,CTOVERLAPPED*);			/* write poll list item		*/
# extern	BOOL	CTAPICALL	ctListData(HANDLE,void*,DWORD,DWORD);				/* get list data		*/
# extern	HANDLE	CTAPICALL	ctListEvent(HANDLE,DWORD);					/* get list event		*/
# extern  BOOL	CTAPICALL  	ctGetNumberOfLicenses(HANDLE, SHORT*, BYTE);		/* Key Check CTAPI interface */
