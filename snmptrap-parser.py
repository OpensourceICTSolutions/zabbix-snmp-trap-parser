#!/usr/bin/env python
# All rights reserved Opensource ICT Solutions B.V.
# Free to redistribute with mention to Opensource ICT Solutions

# For use with Zabbix
# Place in directory
# Update snmptrapd.conf to use this script:
#  disableAuthorization yes
#  traphandle default /usr/bin/python <location of this script>
# And start Zabbix stuffs

import re
import sys
import time


def main():
    destination = "/tmp/zbx_traps.tmp"  # File destination

    # Getting Trap
    trap = sys.stdin.readlines()  # Read from stdin
    r = "".join(trap)  # Convert LIST to STRING

    # Format the time string
    formatted_time = str(time.strftime("%H:%M:%S %Y/%m/%d"))

    # Matching on IPaddress
    source = re.findall(".snmpTrapAddress.0 ([\d.+]+)", r)[0]

    # Building the HEADER so that Zabbix understands it
    header = "{0} ZBXTRAP  {1}".format(formatted_time, source)

    # Appending it to the log file for Zabbix to pickup
    with open(destination, "a") as file:
        file.write("{0}\n{1}".format(header, "".join(trap)))


if __name__ == "__main__":
    main()
