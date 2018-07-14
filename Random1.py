#!/usr/bin/python

import random

seq=["Bangalore","Hyderabad","Ooty","Mysore"]
print random.choice(seq)

print random.randrange(1,10)
print random.randrange(1,10,2)

print "random():",random.random()

print "random():",random.random()

random.seed(10)
print"Random number with seed 10:",random.random()

numbers=range(1,10)
random.shuffle(numbers)
print numbers

print random.uniform(10,100)
