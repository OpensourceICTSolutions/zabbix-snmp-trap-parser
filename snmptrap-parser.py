#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Opensource ICT Solutions B.V.
# https://oicts.com
#
#version: 2.0.0
#date: 11-02-2021
#
#All rights reserved Opensource ICT Solutions B.V.
#Free to redistribute with mention to Opensource ICT Solutions
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.


# For use with Zabbix
# Place in directory
# Update snmptrapd.conf to use this script:
#  disableAuthorization yes
#  traphandle default /usr/bin/python3.6 <location of this script>
# And start Zabbix stuffs

import re
import sys
import time
import subprocess

# Trap write location:
destination = "/tmp/snmptrap.log"  # File destination

# Getting Trap
trap = sys.stdin.readlines()  # Read from stdin
trap.pop(0)
result = "" #Declare empty variable
r = "".join(trap)  # Convert LIST to STRING

# Format the time string
time = time.strftime("%H:%M:%S %Y/%m/%d")
time = str(time)

# Matching on IPaddress
source = re.findall('UDP:.\[([\d.+]+)\]' ,r)

# Building the HEADER so that Zabbix understands it
HEADER = ''.join(source)
IP = str(source).strip("[]'")
HEADER = time + " ZBXTRAP  " +  str(IP)

# Appending it to the log file for Zabbix to pickup
with open(destination, "a") as file:
    file.write (HEADER + "\n" + r)
