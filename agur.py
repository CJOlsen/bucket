#! /usr/bin/python
## agur.py - Apt-Get Update Reminder (for conky)
## Author: Christopher Olsen

## a little script to calculate the time passed since the last apt-get upgrade.
## the time value is stored in agur.days and gets updated once an hour by a
## cronjob.  that file is referenced by conky to display the elapsed time (in
## days) since apt-get upgrade

import datetime

hist_loc = "/var/log/apt/history.log"
hist_log = open(hist_loc, 'r')
file_txt = hist_log.readlines()

# make a list of 3-tuples, 1st must include "apt-get upgrade", 2nd is the 
# upgraded stuff, 3rd is the timestamp
upgrades = [(file_txt[i],file_txt[i+1],file_txt[i+2])
            for i 
            in range(len(file_txt)) 
            if "apt-get upgrade" in file_txt[i]]

end_date_raw = upgrades[-1][-1].split(' ')

date_parts = end_date_raw[1].split('-')
day, month, year = int(date_parts[2]), int(date_parts[1]), int(date_parts[0])

time_parts = end_date_raw[-1][:-1].split(':') 
hour, minute, second = int(time_parts[0]), int(time_parts[1]),int(time_parts[2])

upgr_time = datetime.datetime(year, month, day, hour, minute, second)
time_passed = datetime.datetime.now() - upgr_time
days_passed = '%.2f' % (time_passed.total_seconds()/60./60/24)

outfile = open(***/path/to/scripts***+'/agur.days', 'w')
outfile.write("#!/bin/sh\n\n")
outfile.write("## see agur.py for details\n\n")
outfile.write(' '.join(["echo", days_passed]))
outfile.close()




