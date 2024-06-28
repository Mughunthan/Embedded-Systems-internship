from machine import Pin
import time
trigger=Pin(15,Pin.OUT)
echo=Pin(14,Pin.IN)
l=Pin(2,Pin.OUT)

l2=Pin(3,Pin.OUT)

while(1):
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
       signaloff = time.ticks_us()
    while echo.value() == 1:
       signalon = time.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2 
    print("Total distance",distance,"cm")
    print("sensor")
    time.sleep(1)
    if distance<50 :
        l.on()
        l2.off()
    elif distance<100:
        l.off()
        l2.on()
        
    else:
        l.on()
        l2.on()
            