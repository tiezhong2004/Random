import pyctapi
cti = pyctapi.pyCtApi()





cti.Open("AUHVSAPP8", "intouch", "intouchss")
print "Result", cti.TagReadStr("HVOMET__WIND_SPEED_1M")

cti.Close()

cti.Open("AUHVSAPP9", "intouch", "intouchss")
print "Result", cti.TagReadStr("HVOMET__WIND_SPEED_1M")

cti.Close()

raw_input("Close")