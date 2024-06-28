from  machine import Pin
from time import sleep
#led=Pin(2,Pin.OUT)
relay=Pin(7,Pin.OUT)
while(1):
    relay.on()
    sleep(1)
    relay.off()
    sleep(1)

    