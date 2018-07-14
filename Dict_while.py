#!/usr/bin/python
import random
dict={}
while(len(dict)<100):
	Number=random.randrange(100,250)
	if dict.has_key(Number):
		dict[Number]+=1
	else:
		dict[Number]=1
print dict.items()

print " The min occurances %d"%(min(dict.values()))
print " The max occurances %d"%(max(dict.values()))
