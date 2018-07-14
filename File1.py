#!/usr/bin/python

fh=open("Sample.txt","r")

dir(fh)

print "Name of the file",fh.name
print "Opening Mode ",fh.mode
print "State of the file (checking for close)",fh.closed

string=fh.readlines()
word_count=0
char_count=0
for line in string:
	word_count +=len(line.split())
	char_count +=len(line)

print "Number of lines in file {0} is {1}".format(fh.name,len(string))
print "Number of words in file {0} is {1}".format(fh.name,word_count)
print "Number of chars in file {0} is {1}".format(fh.name,char_count)

fh.close()

