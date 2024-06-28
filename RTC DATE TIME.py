# RTC.py
import machine
from machine import Pin
import utime

rtc=machine.RTC()
rtc.datetime((2023, 2, 28, 7, 23, 59, 5, 0))    #y m d | weekday | h m s | sub-seconds     


while True:

   timestamp=rtc.datetime()
   timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
   print(timestring)
   utime.sleep(1)