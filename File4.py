#!/usr/bin/python
fh=open("Sample_01.txt","r")
dir(fh)
print"Name of the file",fh.name
print"File opening mode",fh.mode
print" File closing state ",fh.closed
string=fh.readlines()
words=[]
for line in string:
	words.extend(line.split())
print "Number of lines in file {0} is {1}".format(fh.name,len(string))
print "Number of words in file {0} is {1}".format(fh.name,len(words))
fh.close()

dict={}
for word in words:
	if dict.has_key(word):
		dict[word]+=1
	else:
		dict[word]=1
print dict.items()
