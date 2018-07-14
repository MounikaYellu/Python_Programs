#!/usr/bin/python

fh=open("Sample_01.txt","r")
dir (fh)

print "Name of the file",fh.name
print "Mode of the file",fh.mode
print "Checking for closed state ",fh.closed 
string = fh.readline()
print string
print fh.tell()
fh.seek(0,0)
string=fh.readline()
print string
fh.close()
