#!/usr/bin/python

pattern = range(0,16)

from random import shuffle

shuffle(pattern)

# Generate the pattern

while(len(pattern)>4):
	array = []
	for i in range(4):
		array.append(pattern.pop())
	pattern.insert(0,array)

# Display the matrix format

def display():
	global pattern
	from os import system
	system("clear")
	for each_row in pattern:
		for each_element in each_row:
			print "%02d \t"%(each_element),
		print " "

# Get position

def get_pos():
	global pattern
	for each_row in pattern:
		if each_row.count(0):
			return pattern.index(each_row),each_row.index(0)

# Get move

def get_move():
	pass

# Validate move

def validate_move():
	pass
display()
print get_pos()
