import time

ticks=time.time()
print "Number of ticks since 12:00am jan1,1970:",ticks

localtime=time.localtime(time.time())
print "Local current time:",localtime

localtime=time.asctime(time.localtime(time.time()))
print "Local current time:",localtime

import calendar
cal=calendar.month(2018,7)
print "Here is the calendar"
print cal
