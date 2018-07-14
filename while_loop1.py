#!/usr/bin/python
numbers=range(1,10)
count=0
while(count<9):
	if count==5:
		count+=1
		pass
		continue
	print numbers[count]
	count+=1
