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

printf "%(%H:%M:%S %Y/%m/%d)T ZBXTRAP $destination \r\n $NUM \r\n $host \r\n $ip \r\n $vars\r\n">> /tmp/zabbix_traps.tmp
