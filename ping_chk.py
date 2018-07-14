#!/usr/bin/python

from commands import getstatusoutput

def ping_check(ipaddress):
	ping_response = getstatusoutput("ping -c 6 {0}".format(ipaddress))
	
	if ping_response[0] == 0:
		return True
	else:
		return False

print ping_check("localhost")
print ping_check("192.168.179.139")
print ping_check("192.168.179.130")
