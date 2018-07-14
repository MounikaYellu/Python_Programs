#!/usr/bin/python
fh=open("Data","w")
print dir(fh)
print "Name of the file",fh.name
print "Mode of the file",fh.mode
print "status checking for close ",fh.closed
fh.write("Hello,python")
fh.close()
