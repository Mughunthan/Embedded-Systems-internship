from machine import Pin
from time import sleep 
led=Pin(2,Pin.OUT)
led2=Pin(3,Pin.OUT)

while(1):
    led.off()
    led2.off()
    sleep(1)
    
    led.off()

    led2.on()
    sleep(1)

    led.on()
    led2.off()
    sleep(1)
    
    led.on()
    led2.on()
    sleep(1)
    