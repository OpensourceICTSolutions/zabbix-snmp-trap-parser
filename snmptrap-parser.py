#!/usr/bin/env python
#All rights reserved Opensource ICT Solutions B.V.
#Free to redistribute with mention to Opensource ICT Solutions
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
