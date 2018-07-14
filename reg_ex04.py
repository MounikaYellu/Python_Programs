import re

phone="2018-967-987 # This is Phone Number"

num=re.sub(r'#.*$',"",phone)
print "Phone Num:",num

num=re.sub(r'\D',"",phone)
print "Phone Num:",num
