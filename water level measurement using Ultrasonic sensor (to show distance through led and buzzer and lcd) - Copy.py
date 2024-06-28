from machine import Pin
from gpio_lcd import GpioLcd
import time
trigger=Pin(15,Pin.OUT)
echo=Pin(14,Pin.IN)
l=Pin(2,Pin.OUT)
buz=Pin(6,Pin.OUT)
l2=Pin(3,Pin.OUT)
l3=Pin("LED",Pin.OUT)
lcd = GpioLcd(rs_pin = Pin(8),
          enable_pin = Pin(9),
          d4_pin = Pin(10),
          d5_pin = Pin(11),
          d6_pin = Pin(12),
          d7_pin = Pin(13))

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
    lcd.move_to(0,0) 
    lcd.putstr("DISTANCE VAL")
    lcd.move_to(0,1) 
    lcd.putstr(str(distance))
    
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
    elif distance<50 and distance>20:
        l.off()

        l2.off()
        l3.on()
        buz.off()
    else:
        l.off()
        l2.off()
        l3.off()
        buz.on()
        
        
        
            