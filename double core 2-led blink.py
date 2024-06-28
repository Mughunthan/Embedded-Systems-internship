from machine import Pin
from time import sleep
import _thread
led=Pin(2,Pin.OUT)
led2=Pin(3,Pin.OUT)

def s():
 while(1):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
_thread.start_new_thread(s,())
while(1):   
    led2.on()
    sleep(0.1)
    led2.off()
    sleep(0.1)

    
    

     