#!/usr/bin/python

lst=[123,'xyz','zara','abc','xyz']
print lst

lst.reverse()
print lst

print lst[::-1]

lst.remove('xyz')
print "List:",lst

lst.remove('abc')
print "List:",lst

lst.sort()

print lst
