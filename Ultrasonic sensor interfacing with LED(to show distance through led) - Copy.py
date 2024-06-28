from machine import Pin
import time
trigger=Pin(15,Pin.OUT)
echo=Pin(14,Pin.IN)
l=Pin(2,Pin.OUT)
buz=Pin(6,Pin.OUT)
l2=Pin(3,Pin.OUT)
l3=Pin("LED",Pin.OUT)

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
    if distance>80 :
        l.on()
        l2.off()
        l3.off()
        buz.off()
    elif distance<80 and distance>50:
        l.off()
        l2.on()
        l3.off()
        buz.off()
    elif distance<20 and distance>10:
        l.off()
        l2.off()
        l3.on()
        buz.off()
    else:
        l.off()
        l2.off()
        l3.off()
        buz.on()
            