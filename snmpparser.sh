#!/bin/bash
#All rights reserved Opensource ICT Solutions B.V.
#Free to redistribute with mention to Opensource ICT Solutions

read host
read ip
vars=


while read oid val
do
  if [ "$vars" = "" ]
  then
    vars="$oid = $val"
  else
    vars="$vars, $oid = $val"
  fi
done


[[ ${host} =~ ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) ]] && NUM=${BASH_REMATCH}

printf "ZBXTRAP $NUM\r\n$host $ip $vars\r\n">> /tmp/zabbix_traps.tmp
