# temp.py - measures & logs temperature in log file
# script template: https://stackoverflow.com/a/57274737
# setup cronjobs: https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804

import time
import datetime
import logging

#logging.basicConfig(filename='temp.log', encoding='utf-8', level=logging.INFO)

currentTime = datetime.datetime.now()
with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
	currentTemp = File.readline()

#logging.info(str(currentTime) + " - " + str(float(currentTemp) / 1000))
print(f'{currentTime} -- {float(currentTemp)/1000}°C')
