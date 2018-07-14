#!/usr/bin/python
str="This is string example..."
print "str.capitalize():",str.capitalize()

sub='i'
print "str.count(sub,4,40):",str.count(sub,4,40)

sub="amp"
print"str.count(sub):",str.count(sub)

str1="This is string example..."
str2="exam"

print str1.find(str2)
print str1.find(str2,10)
print str1.find(str2,40)

str1="This is string example..."
str2="exam"

print str1.index(str2)
print str1.index(str2,10)
print str1.index(str2,40)
