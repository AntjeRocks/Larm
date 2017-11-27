# Larm

Larm is a monitoring tool which alarms you via smtp mail

### Usage

**python3 monitoring.py** -> this operation will monitor all options

**python3 monitoring.py -o disk** -> this allows you to perform a single monitoring request

hf



crontab example: 

*/1 * * * * /usr/bin/python3 /media/vbox/Larm/monitoring.py
