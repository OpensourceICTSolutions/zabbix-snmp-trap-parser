# zabbix-snmp-traps-script

These scripts are built for RHEL8 (Centos8). Due to the removal of net-snmp-perl in RHEL8, we can no longer use SNMP Traps in Zabbix as they won't be parsed. See bug report: https://support.zabbix.com/browse/ZBX-17192

Use: 

snmpparser.sh for bash

snmptrap-parser.py for python

For more info on how to install check out the tutorial:
https://blog.zabbix.com/parsing-snmp-traps-with-python-or-bash-a-net-snmp-perl-alternative/11577/
