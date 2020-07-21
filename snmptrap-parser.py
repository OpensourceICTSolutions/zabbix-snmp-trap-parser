####
#For use with Zabbix
#Place in directory
#point snmptrapd.conf to it:
# disableAuthorization yes
# traphandle default /usr/bin/python /usr/bin/snmptrap.py
#And start zabbix stuffs

import sys
import re
import time

#Where to write to:
destination = "/tmp/zbx_traps.tmp"


###Getting Trap####
trap = sys.stdin.readlines() #Receive stuff
result = "" #Declare empty variable
r = result.join(trap) # Convert LIST to STRING
######


###Converting again###
#MESSAGE = ''.join([line.strip() for  line in r])
######

######
time = time.strftime("%H:%M:%S %Y/%m/%d")
time = str(time)
######

###Matching on IPaddress###
source = re.findall('.snmpTrapAddress.0 ([\d.+]+)',r)
######

###Building the HEADER so that Zabbix understands it###
HEADER = time + " ZBXTRAP  " + ''.join(source)
######


###Appending it to the log file for Zabbix to pickup###
with open(destination, "a") as file:
    file.write (HEADER + "\n" + r)
######