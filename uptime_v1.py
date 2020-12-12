#!/usr/bin/python3.7
# Parissa Bakhshi
# Project: Checking the system uptime every 10 mins, and then converting it into a year, hh:mm:ss format. This code, triggers an assertion in case uptime is more than 10 mins.
import datetime
import time
def uptime_gen():
    while True:
        with open("/proc/uptime") as f:
            uptime_sec = f.readline().split()
        yield uptime_sec[0]
    

uptime_gen = uptime_gen()

while True:
    time.sleep(600)
    secs = float(next(uptime_gen))
    message = f"Warning! System has been restarted {datetime.timedelta(seconds = secs)} ago"
    try:
        assert float(next(uptime_gen)) > 600, message 
    except AssertionError as e:
        print (e.args[0])
        continue



