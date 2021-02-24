# Zabbix SNMP Trap parser scripts
Welcome to the Opensource ICT Solutions GitHub, where you'll find all kinds of usefull Zabbix resources. These scripts are scripts written in either Python or Bash which will enable us to parse SNMP traps to our Zabbix server.

These scripts are built for RHEL8 (Centos8). Due to the removal of net-snmp-perl in RHEL8, we can no longer use SNMP Traps in Zabbix as they won't be parsed. See bug report: https://support.zabbix.com/browse/ZBX-17192

## How to use the scripts
First things first. Pick your flavor, as we made two scripts available for flexibility 

```
snmpparser.sh for bash
```
```
snmptrap-parser.py for python
```

For more info on how to install check out the tutorial:

https://blog.zabbix.com/parsing-snmp-traps-with-python-or-bash-a-net-snmp-perl-alternative/11577/

For more content like this, check out our Zabbix book:

https://www.amazon.com/Zabbix-Infrastructure-Monitoring-Cookbook-maintaining/dp/1800202237
