#!/usr/bin/python
dict={'Name':"Mounika",'Age':24,"Emp Id":1554}
print dict
#copy a dict
dict2=dict.copy()
print dict2

print dict.get('Namex',"Unknown")
print dict.items()

if dict.has_key('Name'):
	print dict

print dict.setdefault('Age',100)

dict1={'City':"Hyderabad"}
dict.update(dict1)

print dict1

if cmp(dict,dict1):
	print "Same"
print dict

#clear a dict

dict.clear()

print dict

# delete dict

del dict

print dict
