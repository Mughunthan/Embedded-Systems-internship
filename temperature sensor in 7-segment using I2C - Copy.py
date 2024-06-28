import pcf8574
from machine import I2C,Pin,ADC
from time import sleep
import array as a
pot=ADC(27)    #temperature sensor(LM 35)
cv=3300/65535
temp=0
display_21=0
display_22=0

m=a.array('i',[0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f])

i2c=I2C(id=0,scl=Pin(21),sda=Pin(20),freq=100000)
p=pcf8574.PCF8574(i2c,0x21)
p.port=0x00
p=pcf8574.PCF8574(i2c,0x20)
p.port=0x00
sleep(1)

while(1):
    if(temp<=99):
        display_21=temp%10
        display_22=temp/10
        temp=int(pot.read_u16()*cv/10)
        p=pcf8574.PCF8574(i2c,0x21)
        p.port=m[int(display_21)]
        p=pcf8574.PCF8574(i2c,0x20)
        p.port=m[int(display_22)]
        print(temp)
    sleep(3)
       
