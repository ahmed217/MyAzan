#!/usr/bin/env python3

# this is controlled by a service in 
# /lib/systemd/system/azan.service

import schedule
import time
from datetime import date 

from player import AzanPlayer
from praytimes import PrayTimes  

# this one only plays azan   
def azanjob(flag):
  ap = AzanPlayer()
  if(flag == 'fajr'): 
    ap.play('./mp3/fajr/')
    print(' : Fajr')
  else:
    ap.play()
    print(' : other')

# this one schedules azan time every night at 2:00am
 
def schedulejob():
  #cancel all azan and reschedule because everyday there is little time change of each salat
  schedule.clear('azan-tasks')
  pt = PrayTimes('Karachi')
  pt.adjust({'asr': 'Hanafi','maghrib': '-1 min'})

  memphis = (35.0387, -89.9276)
  times = pt.getTimes(date.today(), memphis, -6, 1)  

  lst = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
  for i in lst:
    print('Scheduling '+i+ ': '+ times[i.lower()])
    schedule.every().day.at(times[i.lower()]).do(lambda: azanjob(i)).tag('azan-tasks')


#run it now and schedule it at 2:00a 
schedulejob()

# this scheduler everyday at 1:00am 
schedule.every().day.at("01:00").do(schedulejob)

while True:
    schedule.run_pending()
    time.sleep(1)
