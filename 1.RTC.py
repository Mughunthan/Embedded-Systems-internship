import machine
from machine import Pin
import utime

rtc=machine.RTC()
rtc.datetime((2023, 2, 28, 2, 23, 59, 0, 0))


while True:

   timestamp=rtc.datetime()
   timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
   print(timestring)
   utime.sleep(1)
