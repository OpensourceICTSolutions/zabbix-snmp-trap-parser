#!/bin/bash
# -*- coding: utf-8 -*-
#
# Copyright 2021 Opensource ICT Solutions B.V.
# https://oicts.com
#
#version: 1.0.0
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

read host
read ip
vars=


while read oid val
do
  if [ "$vars" = "" ]
  then
    vars="$oid = $val \r\n"
  else
    vars="$vars \r\n $oid = $val"
  fi
done


#[[ ${host} =~ ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) ]] && NUM=${BASH_REMATCH}
# printf "%(%H:%M:%S %Y/%m/%d)T ZBXTRAP $NUM\r\n$host $ip $vars\r\n">> /tmp/zabbix_traps.tmp
#echo trap: $1 $host $ip $vars 



sourceAndDest=$(grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' <<< $ip) 
stringarray=($sourceAndDest) 
source=${stringarray[0]} 
destination=${stringarray[1]}

printf "%(%H:%M:%S %Y/%m/%d)T ZBXTRAP $source \r\n $NUM \r\n $host \r\n $ip \r\n $vars\r\n">> /tmp/zabbix_traps.tmp
