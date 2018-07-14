def printme(str):
	print str
	return
printme("I'm the first call to user defined function!")
printme("Again second call to the same function")

def changeme(mylist):
	mylist.append([1,2,3,4])
	print "Values inside the function:",mylist
	return

mylist=[10,20,30]
changeme(mylist)
print "Values outside the function:",mylist

def printinfo(name,age):
	print "Name:",name
	print "Age",age
	return
printinfo("mounika",24)
printinfo(age=89,name="miki")

