#!/usr/bin/env python

class Employee:
	empCount=0
	def __init__(self,dict):
		for key in dict:
			setattr(self,key,dict[key])
		Employee.empCount+=1
	def displayCount(self):
		print "Total Employee %d"%Employee.empCount
	def displayEmployee(self):
		print "Name:",self.name,",Salary:",self.salary
	def __del__(self):
		class_name=self.__class__.__name__
		print class_name,"destroyed"

emp1=Employee({'name':"Mounika",'salary':"100000"})
emp2=Employee({'name':"Kathya",'salary':"200000"})

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d"%Employee.empCount

print hasattr(emp1,'age')
try:
	print getattr(emp1,'age')
except AttributeError as e:
	print e
print setattr(emp1,'age',8)
print hasattr(emp1,'age')
print getattr(emp1,'age')

print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__

delattr(emp1,'age')

del(emp1)













