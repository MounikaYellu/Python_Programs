#!/usr/bin/python
dict={"Name":"Mounika","Age":24}

try:
	'2'+2
except TypeError:
	print "TypeError Exception triggered"

try:
	dict['Address']
except KeyError:
	print "KeyError Exception is raised"
except NameError:
	print "Name Error is raised"
else:
	print "The key value is {0}".format(dict['Name'])
finally:
	print "I am here"

try:
	fh=open("Sample.txt","r")
except IOError:
	print "IOError raised as the file doesn't exist"
else:
	print "File exists and is opened"
fh.close()

try:
	a+2
except NameError:
	print "NameError Exception triggered"


