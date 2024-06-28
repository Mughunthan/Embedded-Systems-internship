from machine import Pin,ADC
from time import sleep
from gpio_lcd import GpioLcd
relay=Pin(7,Pin.OUT)
pot=ADC(27)    #temperature sensor(LM 35)
cv=3300/65535
lcd = GpioLcd(rs_pin = Pin(8),
          enable_pin = Pin(9),
          d4_pin = Pin(10),
          d5_pin = Pin(11),
          d6_pin = Pin(12),
          d7_pin = Pin(13))
while(1):
    temp=int(pot.read_u16()*cv/10)
    
    lcd.move_to(0,0)
    lcd.putstr(str(temp) +" "+"C"+" ")
    print(temp)
    sleep(1)
    lcd.move_to(0,1)
            
    
    

    