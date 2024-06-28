from machine import Pin,ADC,PWM
from time import sleep
from gpio_lcd import GpioLcd
lcd = GpioLcd(rs_pin = Pin(8),
          enable_pin = Pin(9),
          d4_pin = Pin(10),
          d5_pin = Pin(11),
          d6_pin = Pin(12),
          d7_pin = Pin(13))
pot=ADC(28)
led=PWM(Pin(3))
led.freq(100)
cv=300/65535

while(1):
    val=int(pot.read_u16())
    lcd.move_to(0,0)
    lcd.putstr(str(int(val*cv)))
    print(int(val*cv)) 
    led.duty_u16(val)
    sleep(0.5)
 
